#!/usr/bin/env python3
"""
Test Python API Handler Script
This is a test file for workflow testing in folder 3.
"""

import json

class APIHandler:
    def __init__(self):
        self.base_url = "https://api.example.com"
    
    def get_data(self, endpoint):
        """Simulate API data retrieval"""
        return {"status": "success", "endpoint": endpoint}
    
    def post_data(self, endpoint, data):
        """Simulate API data posting"""
        return {"status": "posted", "data": data}

if __name__ == "__main__":
    handler = APIHandler()
    print("API Handler Test")
    print(handler.get_data("/test"))

