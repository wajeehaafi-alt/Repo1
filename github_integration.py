#!/usr/bin/env python3
"""
GitHub Integration Module
Handles GitHub API interactions for repository sync
"""

import requests
from typing import Dict, Optional

class GitHubIntegration:
    def __init__(self, token: str):
        self.token = token
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
    
    def get_repository(self, owner: str, repo: str) -> Dict:
        """Fetch repository information"""
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def create_pull_request(self, owner: str, repo: str, title: str, 
                           head: str, base: str, body: str) -> Dict:
        """Create a pull request"""
        url = f"{self.base_url}/repos/{owner}/{repo}/pulls"
        data = {
            "title": title,
            "head": head,
            "base": base,
            "body": body
        }
        response = requests.post(url, json=data, headers=self.headers)
        return response.json()

print("GitHub Integration module loaded")

