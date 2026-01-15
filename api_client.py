#!/usr/bin/env python3
"""
API Client for GitHub repository operations
Handles API requests for sync operations
"""

import requests

class APIClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github.v3+json'
        }
    
    def get_repository(self, owner, repo):
        """Fetch repository information"""
        url = f"{self.base_url}/repos/{owner}/{repo}"
        response = requests.get(url, headers=self.headers)
        return response.json()

client = APIClient("https://api.github.com", "test_token")
print("API Client initialized")

