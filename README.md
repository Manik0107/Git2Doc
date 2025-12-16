# 📚 Code2Doc

**Automated Git Repository to Documentation Converter**

Code2Doc is an intelligent documentation generator that transforms GitHub repositories into comprehensive, structured documentation using AI-powered analysis. It leverages advanced language models to understand code structure, extract key information, and generate human-readable documentation automatically.

---

## 🌟 Features

- **🤖 AI-Powered Analysis**: Uses Google's Gemini 2.5 Flash model for intelligent code understanding
- **📂 Repository Scanning**: Automatically analyzes entire GitHub repositories
- **🔍 Smart Extraction**: Identifies functions, classes, dependencies, and code relationships
- **📝 Comprehensive Documentation**: Generates detailed explanations of code functionality
- **🔐 Secure Authentication**: GitHub token-based access for private repositories
- **⚡ Fast Processing**: Efficient analysis powered by the Agno framework

---

##  Usage

### Basic Example

```python
import os
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.github import GithubTools

# Load environment variables
load_dotenv()

# Initialize the agent
agent = Agent(
    model=Gemini("gemini-2.5-flash"),
    instructions=[
        "Use your tools to answer questions about the repo: https://github.com/username/repo",
        "Do not create any issues or pull requests unless explicitly asked to do so",
    ],
    tools=[GithubTools(access_token=os.getenv("GITHUB_ACCESS_TOKEN"))],
)

# Query the repository
response = agent.run("Explain what this repository does")
print(response.content)
```

### Running the Main Script

```bash
# Using Python
python main.py

# Using uv (recommended)
uv run main.py
```

---

## 📄 Sample Output

Code2Doc generates professional documentation in both text and PDF formats:

- **[View Sample Documentation PDF](./simple_document.pdf)** - Click to view the generated documentation

The generated PDF includes:
- ✨ Professional formatting with proper typography
- 📑 Clear heading hierarchy (19.5pt main, 12pt sub, 11.5pt tertiary)
- 🔢 Numbered lists for better organization
- 📝 Comprehensive code analysis with Introduction and Conclusion
- 🎯 Bold formatting for important concepts

> **Note**: Click the PDF link above to view it directly in GitHub's built-in PDF viewer with full scrolling support.

---

## 🛠️ How It Works

1. **Repository Connection**: Connects to GitHub using authenticated API access
2. **Code Analysis**: Scans repository structure, files, and code patterns
3. **AI Processing**: Uses Gemini AI to understand code context and functionality
4. **Documentation Generation**: Creates structured documentation with:
   - File descriptions
   - Function/class explanations
   - Code relationships and dependencies
   - Usage examples
   - Technical insights

---

## 📦 Dependencies

- **agno**: AI agent framework for orchestrating documentation generation
- **google-genai**: Google Gemini AI integration
- **python-dotenv**: Environment variable management
- **crawl4ai**: Web crawling capabilities (optional)

---

## 🎯 Use Cases

- **Project Documentation**: Automatically generate README and docs for your projects
- **Code Understanding**: Quickly understand unfamiliar codebases
- **Onboarding**: Help new team members understand project structure
- **Code Review**: Get AI-powered insights into code functionality
- **Legacy Code**: Document undocumented legacy systems

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Agno Framework**: For providing the AI agent infrastructure
- **Google Gemini**: For powerful language model capabilities
- **GitHub API**: For repository access and analysis

---

## 📧 Contact

**Manik Manavenddram**

- GitHub: [@Manik0107](https://github.com/Manik0107)
- Project Link: [https://github.com/Manik0107/Code2Doc](https://github.com/Manik0107/Code2Doc)

---

## 🗺️ Roadmap

- [ ] Support for multiple output formats (Markdown, HTML, PDF)
- [ ] Batch processing for multiple repositories
- [ ] Custom documentation templates
- [ ] Integration with popular documentation platforms
- [ ] Support for additional programming languages
- [ ] Interactive documentation generation UI
- [ ] Code quality metrics and analysis
- [ ] Automated documentation updates on commits

---



