#!/usr/bin/env python3
"""
Test script to verify GithubTools works correctly
"""
from agno.tools.github import GithubTools
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize GithubTools
tools = GithubTools(access_token=os.getenv("GITHUB_ACCESS_TOKEN"))
repo = "Manik0107/AI_Hiring_Manager"

print("=" * 60)
print("Testing GithubTools")
print("=" * 60)
print(f"Repository: {repo}")
print()

# Test 1: Get repository info
print("Test 1: get_repository()")
try:
    repo_info = tools.get_repository(repo_name=repo)
    print(f"✅ Success!")
    print(f"   Repository info: {str(repo_info)[:200]}...")
    print()
except Exception as e:
    print(f"❌ Failed: {e}")
    print()

# Test 2: Get directory content (root)
print("Test 2: get_directory_content() - root directory")
try:
    files = tools.get_directory_content(repo_name=repo, path="")
    print(f"✅ Success!")
    print(f"   Files found: {len(files) if isinstance(files, list) else 'N/A'}")
    print(f"   Content: {str(files)[:300]}...")
    print()
except Exception as e:
    print(f"❌ Failed: {e}")
    print()

# Test 3: Get repository languages
print("Test 3: get_repository_languages()")
try:
    languages = tools.get_repository_languages(repo_name=repo)
    print(f"✅ Success!")
    print(f"   Languages: {languages}")
    print()
except Exception as e:
    print(f"❌ Failed: {e}")
    print()

# Test 4: Get a specific file (try README.md)
print("Test 4: get_file_content() - README.md")
try:
    readme = tools.get_file_content(repo_name=repo, file_path="README.md")
    print(f"✅ Success!")
    print(f"   Content preview: {str(readme)[:200]}...")
    print()
except Exception as e:
    print(f"❌ Failed: {e}")
    print()

print("=" * 60)
print("Tests completed!")
print("=" * 60)
