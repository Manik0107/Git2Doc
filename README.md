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

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- GitHub Personal Access Token
- Google Gemini API Key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Manik0107/Code2Doc.git
   cd Code2Doc
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using `uv` (recommended):
   ```bash
   uv pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GITHUB_ACCESS_TOKEN=your_github_token_here
   GEMINI_API_KEY=your_gemini_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```

---

## 📖 Usage

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

## 🔑 API Keys Setup

### GitHub Personal Access Token

1. Go to [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Select scopes: `repo`, `read:org`, `read:user`
4. Copy the token and add to `.env`

### Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy the key and add to `.env`

---

## 🎯 Use Cases

- **Project Documentation**: Automatically generate README and docs for your projects
- **Code Understanding**: Quickly understand unfamiliar codebases
- **Onboarding**: Help new team members understand project structure
- **Code Review**: Get AI-powered insights into code functionality
- **Legacy Code**: Document undocumented legacy systems

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

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

<div align="center">

**Made with ❤️ using AI and Open Source**

⭐ Star this repo if you find it useful!

</div>
