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
    ],
    tools=[GithubTools(access_token=os.getenv("GITHUB_ACCESS_TOKEN"))],
)

# Get the content of main.py from the repository
response = agent.run("tell me what is dspy_manim_workflow.py file from the repository doing and what is it about")
print("Response from agent:")
print(response.content)

# # Extract and save the content
# # The agent should return the file content which we can then save
# with open("extracted_main.py", "w") as f:
#     f.write(str(response.content))
    
# print("\nContent saved to extracted_main.py")

