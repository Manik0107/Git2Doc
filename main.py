import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.models.openrouter import OpenRouter
from agno.tools.github import GithubTools

# Load environment variables from .env file
load_dotenv()

# Get user input
print("=" * 60)
print("Code2Doc - Generate Documentation from GitHub Repositories")
print("=" * 60)
print()

github_url = input("Enter the GitHub repository URL: ").strip()
question = input("Enter your question about the repository: ").strip()

print()
print("=" * 60)
print()

# Validate inputs
if not github_url:
    raise ValueError("GitHub URL cannot be empty!")
if not question:
    raise ValueError("Question cannot be empty!")

def parse_github_url(url: str) -> str:
    """
    Extract owner/repo from GitHub URL.
    Examples:
        https://github.com/owner/repo -> owner/repo
        github.com/owner/repo -> owner/repo
        https://github.com/owner/repo.git -> owner/repo
    """
    # Remove protocol
    url = url.replace('https://', '').replace('http://', '')
    # Remove github.com
    url = url.replace('github.com/', '')
    # Remove .git suffix
    url = url.replace('.git', '')
    # Get owner/repo (strip trailing slashes and take first two parts)
    parts = url.strip('/').split('/')
    if len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    raise ValueError(f"Invalid GitHub URL format: {url}")

# Parse GitHub URL to get owner/repo format (required by GithubTools)
try:
    repo_name = parse_github_url(github_url)
    print(f"📦 Repository: {repo_name}")
except ValueError as e:
    print(f"❌ Error: {e}")
    exit(1)


agent = Agent(
    model=OpenRouter(id="google/gemini-2.0-flash-001"),
    instructions=[
        f"You are analyzing the GitHub repository: {repo_name}",
        "You have GithubTools available to read repository data.",
        "",
        "CRITICAL: You MUST use your tools to analyze the ACTUAL repository.",
        "Follow these steps IN ORDER:",
        "",
        f"Step 1: Call get_repository(repo_name='{repo_name}') to get repository details",
        f"Step 2: Call get_repository_languages(repo_name='{repo_name}') to identify programming languages",
        f"Step 3: Call get_directory_content(repo_name='{repo_name}', path='') to list root directory files",
        f"Step 4: Based on the files found, read key files using get_file_content(repo_name='{repo_name}', path='filename')",
        "   - Look for README.md, main files (main.py, app.py, index.js, server.js, etc.)",
        "   - Read package.json, requirements.txt, or similar dependency files",
        "   - Read key source files to understand the codebase",
        "",
        "Step 5: For important directories (like 'src', 'api', 'core', 'components'), call get_directory_content() to explore them",
        "",
        "Provide a COMPREHENSIVE analysis including:",
        "- Repository description and purpose",
        "- Technologies and frameworks used (from languages and dependency files)",
        "- Project structure (directories and their purposes)",
        "- Key files and their roles",
        "- Main functionality and features (from README and code)",
        "- Dependencies and integrations",
        "- Entry points and workflow",
        "",
        "DO NOT provide generic descriptions. Use ACTUAL data from the repository you read using your tools.",
    ],
    tools=[GithubTools(access_token=os.getenv("GITHUB_ACCESS_TOKEN"))],
)

# Get repository file analysis
print("🔍 Analyzing repository files...")
print(f"   Note: Using GithubTools to read {repo_name}")

# Create a specific, actionable prompt
analysis_prompt = f"""Analyze the GitHub repository **{repo_name}** by actually reading it using your GithubTools.

REQUIRED STEPS (use your tools):
1. Get repository info: get_repository(repo_name="{repo_name}")
2. Get languages: get_repository_languages(repo_name="{repo_name}")  
3. List root files: get_directory_content(repo_name="{repo_name}", path="")
4. Read README.md if it exists
5. Identify and read main/entry point files
6. Read dependency files (package.json, requirements.txt, etc.)
7. Explore key directories

After gathering this data, provide a detailed analysis of the repository's:
- Purpose and description
- Technologies used
- Architecture and structure  
- Key features
- Dependencies

{question}

IMPORTANT: Actually call the GitHub tools listed above. Don't skip this step!"""

response = agent.run(analysis_prompt)

# Create documentation agent with proper Agno configuration
documenter = Agent(
    name="DocumentationSpecialist",
    model=OpenRouter(id="google/gemini-2.0-flash-001"),
    description="Software documentation specialist that produces formal technical documentation from repository analysis",
    
    # Instructions - consolidated into clear, structured format
    instructions="""You are a software documentation specialist responsible for producing formal project documentation.

INPUT CONTEXT:
- You will receive detailed descriptions of source files, modules, or workflows extracted from repository analysis
- The input may be analytical, step-based, or fragmented
- The content represents observed behavior and structure, not opinions

OBJECTIVE:
Convert the input into professional, document-level technical explanations suitable for:
- Software design documentation
- System architecture documentation
- Internal technical manuals
- Academic or enterprise project reports

CONSTRAINTS:
- Do not use marketing language
- Do not address the reader directly
- Do not mention prompts, agents, or task instructions
- Do not speculate beyond the provided input
- Do not copy input text verbatim
- Maintain technical accuracy and clarity

OUTPUT REQUIREMENTS:
- Create a COMPREHENSIVE technical document that covers ALL aspects of the code
- MUST start with an **Introduction** section that provides:
  * Overview of the project/file purpose
  * High-level summary of what the code accomplishes
  * Context and motivation for the implementation
  * Target audience and use cases
- Use clear markdown headings (# for main sections, ## for subsections)
- Document EVERY function, class, and method with:
  * Purpose and functionality
  * Parameters and return values
  * Key implementation details
- Document ALL dependencies and imports with their purpose
- Explain the complete workflow and execution flow step-by-step
- Detail ALL algorithms, data structures, and design patterns used
- Include error handling, configuration, and environment setup
- Document ALL external integrations (APIs, databases, file systems)
- Use **bold** formatting for important concepts, key terms, and critical components
- Structure content logically: Introduction → Overview → Architecture → Components → Implementation Details → Integration → Conclusion
- MUST end with a **Conclusion** section that provides:
  * Summary of key features and capabilities
  * Main takeaways and important points
  * Potential use cases or applications
  * Future considerations or extensibility points
- Write for readers without prior knowledge of the implementation
- Use proper technical terminology and formal language
- Be thorough and detailed - this documentation should serve as a complete technical reference""",
    
    # Expected output format
    expected_output="Comprehensive technical documentation in markdown format with clear sections, detailed explanations, and professional technical writing",
    
    # Enable markdown output
    markdown=True,
    
    # Add the repository analysis to additional context instead of knowledge parameter
    # (knowledge parameter expects Knowledge object, not string)
    additional_context=f"""REPOSITORY ANALYSIS:

{response.content}

Use the above repository analysis to generate comprehensive technical documentation.

IMPORTANT: After the Introduction section and before the Architecture/Components sections, you MUST include the following EXACT line on its own line:
[WORKFLOW_DIAGRAM_PLACEHOLDER]

This placeholder will be replaced with the actual workflow diagram image.""",
    
    # Enable search in context
    search_knowledge=False,  # We're using additional_context, not a knowledge base
)

# Generate documentation
print("📝 Generating documentation...")
response1 = documenter.run("Generate comprehensive technical documentation for the analyzed repository file")

# Get the documentation content
doc_content = str(response1.content)

# Save the documentation (with placeholder for now)
output_file = "content.txt"
with open(output_file, "w") as f:
    f.write(doc_content)
    
print(f"✅ Documentation saved to {output_file}")

# Generate initial PDF (without workflow diagram)
print("📄 Generating initial PDF...")
from doc_creation import generate_pdf
# We'll regenerate the PDF after the workflow diagram is created

# WORKFLOW GENERATION AGENT


print()
print("=" * 60)
print("🔄 Generating Workflow Diagram JSON...")
print("=" * 60)
print()

# Create workflow generation agent
workflow_agent = Agent(
    name="WorkflowArchitect",
    model=OpenRouter(id="google/gemini-2.0-flash-001"),
    description="Software architecture specialist that analyzes repository structure and generates workflow diagrams in JSON format",
    
    instructions="""You are a software architecture specialist responsible for analyzing code repositories and generating HIGH-LEVEL workflow diagrams.

INPUT CONTEXT:
- You will receive detailed repository analysis containing information about files, modules, functions, classes, and dependencies
- The analysis describes the structure, components, and relationships within the codebase

OBJECTIVE:
Generate a SIMPLIFIED, HIGH-LEVEL workflow diagram in JSON format that visualizes ONLY the main architecture and data flow.

CRITICAL SIMPLIFICATION RULES:
- **MAXIMUM 5-10 NODES TOTAL** - Focus on main workflow stages only
- **EXCLUDE low-level details**: No individual function calls, environment loading, configuration, instruction/prompt nodes, or intermediate variables
- **INCLUDE only**: Entry points, major processing stages, external services, final outputs
- Show the BIG PICTURE workflow, not implementation details

JSON STRUCTURE REQUIREMENTS:
You MUST generate a JSON object with this EXACT structure:

{
  "meta": {
    "title": "Project Title Here",
    "layout": "LR"
  },
  "node_types": {
    "entry": {"color": "#1bbcd6", "shape": "box"},
    "core": {"color": "#2e8b57", "shape": "box"},
    "external": {"color": "#d9534f", "shape": "box"},
    "output": {"color": "#7b2d3a", "shape": "box"}
  },
  "nodes": [
    {"id": "unique_id", "label": "Display Name", "type": "entry|core|external|output", "layer": 1}
  ],
  "edges": [
    {"from": "source_node_id", "to": "target_node_id"}
  ]
}

SIMPLIFIED NODE CLASSIFICATION (4 types only):
1. **entry** (Layer 1): Main entry point (e.g., "main.py", "User Input")
2. **core** (Layer 2-3): Major processing stages only (e.g., "Repository Analysis", "Documentation Generation", "PDF Creation")
3. **external** (Layer 2-3): External services/APIs (e.g., "GitHub API", "Gemini AI Model")
4. **output** (Layer 4): Final deliverables only (e.g., "Technical Documentation", "PDF Report", "Workflow Diagram")

LAYER ASSIGNMENT (Simplified):
- Layer 1: Entry point (1 node typically)
- Layer 2-3: Core processing and external services (3-6 nodes)
- Layer 4: Final outputs (1-3 nodes)

EDGE CREATION RULES:
- Show only DIRECT, IMPORTANT data flows
- One arrow per major connection
- No redundant or circular paths
- Keep it linear and simple

WHAT TO EXCLUDE (very important):
- ❌ Individual function calls (load_dotenv, agent.run, etc.)
- ❌ Configuration nodes (instructions, prompts, settings)
- ❌ Intermediate variables or responses
- ❌ Helper utilities unless they're a major component
- ❌ Token/credential nodes unless they're a key external service
- ❌ Environment variables

WHAT TO INCLUDE (focus on these):
- ✅ Main entry script
- ✅ Major processing stages (like "Analyze Repository", "Generate Docs")
- ✅ Key external services (GitHub API, AI Model)
- ✅ Final outputs (PDF, Documentation file)

ANALYSIS APPROACH:
1. Identify the ONE main entry point
2. Identify 2-4 MAJOR processing stages (not individual functions)
3. Identify 1-2 KEY external services
4. Identify 1-3 final outputs
5. Draw simple, direct connections between them
6. Generate minimal, clean JSON structure

EXAMPLE for a documentation generator:
- Entry: "main.py" → Core: "Repository Analyzer" → External: "GitHub API"
- Core: "Repository Analyzer" → Core: "Documentation Generator" → External: "AI Model"
- Core: "Documentation Generator" → Output: "Technical PDF"
Total: ~6 nodes, clean and readable

Remember: Return ONLY valid JSON, nothing else. Keep it SIMPLE and HIGH-LEVEL.""",
    
    expected_output="Valid JSON object representing the workflow diagram with meta, node_types, nodes, and edges",
    
    markdown=False,
    
    # Note: We pass the repository analysis directly in the prompt below
    # instead of using additional_context, as it's more reliable
    search_knowledge=False,
)

# Generate workflow JSON
print("🏗️  Analyzing repository architecture...")
workflow_prompt = f"""Based on the following repository analysis, generate a simplified workflow diagram JSON with 5-10 key nodes showing only the high-level workflow stages.

REPOSITORY ANALYSIS:
{response.content}

Remember: Return ONLY valid JSON with the structure: meta, node_types, nodes, and edges. Keep it SIMPLE and HIGH-LEVEL."""
workflow_response = workflow_agent.run(workflow_prompt)

# Extract and clean the JSON content
import json
import re

workflow_json_str = str(workflow_response.content).strip()

# Remove markdown code fences if present
workflow_json_str = re.sub(r'^```json\s*', '', workflow_json_str)
workflow_json_str = re.sub(r'^```\s*', '', workflow_json_str)
workflow_json_str = re.sub(r'\s*```$', '', workflow_json_str)
workflow_json_str = workflow_json_str.strip()

# Try to parse and validate the JSON
try:
    workflow_data = json.loads(workflow_json_str)
    
    # Validate required keys
    required_keys = ["meta", "node_types", "nodes", "edges"]
    missing_keys = [key for key in required_keys if key not in workflow_data]
    
    if missing_keys:
        print(f"⚠️  Warning: Generated JSON is missing required keys: {missing_keys}")
        print("Attempting to fix...")
        
        # Add missing keys with defaults
        if "meta" not in workflow_data:
            workflow_data["meta"] = {"title": "Project Workflow", "layout": "TB"}
        if "node_types" not in workflow_data:
            workflow_data["node_types"] = {
                "entry": {"color": "#1bbcd6", "shape": "box"},
                "core": {"color": "#2e8b57", "shape": "box"},
                "tool": {"color": "#d6c44f", "shape": "box"},
                "external": {"color": "#d9534f", "shape": "box"},
                "compatibility": {"color": "#4f8a8b", "shape": "box"},
                "output": {"color": "#7b2d3a", "shape": "box"}
            }
        if "nodes" not in workflow_data:
            workflow_data["nodes"] = []
        if "edges" not in workflow_data:
            workflow_data["edges"] = []
    
    # Validate node structure
    for node in workflow_data.get("nodes", []):
        required_node_keys = ["id", "label", "type", "layer"]
        missing_node_keys = [key for key in required_node_keys if key not in node]
        if missing_node_keys:
            print(f"⚠️  Warning: Node {node.get('id', 'unknown')} is missing keys: {missing_node_keys}")
    
    # Validate edges reference existing nodes
    node_ids = {node["id"] for node in workflow_data.get("nodes", [])}
    for edge in workflow_data.get("edges", []):
        if edge.get("from") not in node_ids:
            print(f"⚠️  Warning: Edge references non-existent node: {edge.get('from')}")
        if edge.get("to") not in node_ids:
            print(f"⚠️  Warning: Edge references non-existent node: {edge.get('to')}")
    
    # Save the workflow JSON
    workflow_output_file = "project_workflow.json"
    with open(workflow_output_file, "w") as f:
        json.dump(workflow_data, f, indent=4)
    
    print(f"✅ Workflow JSON saved to {workflow_output_file}")
    print(f"   - Nodes: {len(workflow_data.get('nodes', []))}")
    print(f"   - Edges: {len(workflow_data.get('edges', []))}")
    print(f"   - Title: {workflow_data.get('meta', {}).get('title', 'N/A')}")
    
except json.JSONDecodeError as e:
    print(f"❌ Error: Failed to parse workflow JSON: {e}")
    print("Raw response:")
    print(workflow_json_str[:500])  # Print first 500 chars for debugging
    
    # Save the raw response for debugging
    with open("workflow_debug.txt", "w") as f:
        f.write(workflow_json_str)
    print("⚠️  Raw response saved to workflow_debug.txt for debugging")

print()
print("=" * 60)
print("📊 Generating workflow diagram...")
print("=" * 60)
print()

# Generate workflow diagram from the JSON
import subprocess
try:
    result = subprocess.run(
        ["python", "generate_project_workflow.py"],
        capture_output=True,
        text=True,
        timeout=30
    )
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"⚠️  Warning: Workflow diagram generation had issues:")
        print(result.stderr)
except subprocess.TimeoutExpired:
    print("⚠️  Warning: Workflow diagram generation timed out")
except Exception as e:
    print(f"⚠️  Warning: Could not generate workflow diagram: {e}")

print()
print("=" * 60)
print("📝 Inserting workflow diagram into documentation...")
print("=" * 60)
print()

# Update the documentation content with the workflow diagram
workflow_diagram_path = os.path.abspath("project_workflow_diagram.png")
if os.path.exists(workflow_diagram_path):
    # Read the current documentation
    with open(output_file, "r") as f:
        doc_content = f.read()
    
    # Replace the placeholder with the workflow diagram markdown
    diagram_markdown = f"\n## Workflow Diagram\n\n![Project Workflow Diagram]({workflow_diagram_path})\n\n*Figure: High-level workflow architecture of the project*\n"
    
    # Replace placeholder if it exists, otherwise insert after Introduction
    if "[WORKFLOW_DIAGRAM_PLACEHOLDER]" in doc_content:
        doc_content = doc_content.replace("[WORKFLOW_DIAGRAM_PLACEHOLDER]", diagram_markdown)
        print("✅ Workflow diagram placeholder replaced")
    else:
        # Try to insert after Introduction section
        # Look for common patterns: "## Overview", "## Architecture", "## Components"
        insertion_patterns = [
            ("\n## Overview\n", diagram_markdown + "\n## Overview\n"),
            ("\n## Architecture\n", diagram_markdown + "\n## Architecture\n"),
            ("\n## Components\n", diagram_markdown + "\n## Components\n"),
            ("\n## Implementation\n", diagram_markdown + "\n## Implementation\n"),
        ]
        
        inserted = False
        for pattern, replacement in insertion_patterns:
            if pattern in doc_content:
                doc_content = doc_content.replace(pattern, replacement, 1)
                print(f"✅ Workflow diagram inserted before {pattern.strip()}")
                inserted = True
                break
        
        if not inserted:
            # Fallback: insert after first major heading
            lines = doc_content.split('\n')
            insert_index = -1
            for i, line in enumerate(lines):
                if line.startswith('## ') and i > 0:
                    insert_index = i
                    break
            
            if insert_index > 0:
                lines.insert(insert_index, diagram_markdown.strip())
                doc_content = '\n'.join(lines)
                print("✅ Workflow diagram inserted after Introduction")
            else:
                # Last resort: append after first paragraph
                doc_content = doc_content + "\n\n" + diagram_markdown
                print("⚠️  Workflow diagram appended to end of document")
    
    # Save the updated documentation
    with open(output_file, "w") as f:
        f.write(doc_content)
    
    print(f"✅ Updated documentation saved to {output_file}")
    
    # Now regenerate the PDF with the workflow diagram
    print()
    print("📄 Generating final PDF with workflow diagram...")
    generate_pdf(input_file=output_file, output_file="technical_documentation.pdf")
else:
    print("⚠️  Warning: Workflow diagram not found, generating PDF without it")
    generate_pdf(input_file=output_file, output_file="technical_documentation.pdf")

print()
print("=" * 60)
print("✅ All tasks completed!")
print("=" * 60)
print()
print("Generated files:")
print(f"  📄 {output_file} - Technical documentation (with workflow diagram)")
print(f"  📕 technical_documentation.pdf - PDF documentation (with embedded diagram)")
print(f"  🔄 project_workflow.json - Workflow structure")
print(f"  🖼️  project_workflow_diagram.png - Workflow diagram")
print("=" * 60)
