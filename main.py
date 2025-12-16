import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.github import GithubTools

# Load environment variables from .env file
load_dotenv()

agent = Agent(
    model = Gemini("gemini-2.5-flash"),
    instructions=[
        "Use your tools to answer questions about the repo: https://github.com/Manik0107/VATA",
        "Do not create any issues or pull requests unless explicitly asked to do so",
        "When analyzing code files, provide COMPREHENSIVE details including:",
        "- ALL functions and classes with their complete signatures, parameters, and return types",
        "- ALL imports and dependencies (both external libraries and internal modules)",
        "- Complete explanation of the main workflow and execution flow",
        "- ALL key algorithms, logic, and implementation details",
        "- Data structures used (lists, dictionaries, objects, etc.)",
        "- Error handling mechanisms and exception handling",
        "- Configuration and environment variables used",
        "- File I/O operations and external integrations",
        "- API calls, database operations, or external service interactions",
        "- Design patterns and architectural decisions",
        "- Purpose and role of each major code block",
        "Be extremely thorough - extract EVERY important detail that would be needed for complete technical documentation",
    ],
    tools=[GithubTools(access_token=os.getenv("GITHUB_ACCESS_TOKEN"))],
)

# Get repository file analysis
print("🔍 Analyzing repository file...")
response = agent.run("tell me what is dspy_manim_workflow.py file from the repository doing and what is it about")

# Create documentation agent with proper Agno configuration
documenter = Agent(
    name="DocumentationSpecialist",
    model=Gemini("gemini-2.5-flash"),
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

Use the above repository analysis to generate comprehensive technical documentation.""",
    
    # Enable search in context
    search_knowledge=False,  # We're using additional_context, not a knowledge base
)

# Generate documentation
print("📝 Generating documentation...")
response1 = documenter.run("Generate comprehensive technical documentation for the analyzed repository file")

# Save the documentation
output_file = "content.txt"
with open(output_file, "w") as f:
    f.write(str(response1.content))
    
print(f"✅ Documentation saved to {output_file}")

# Generate PDF from the documentation
print("📄 Generating PDF...")
from doc_creation import generate_pdf
generate_pdf(input_file=output_file, output_file="simple_document.pdf")
