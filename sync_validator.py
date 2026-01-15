#!/usr/bin/env python3
"""
Sync validator for workflow testing
Validates bi-directional sync operations
"""

class SyncValidator:
    def __init__(self):
        self.status = "active"
    
    def validate(self, data):
        """Validate sync data"""
        return isinstance(data, dict) and 'source' in data

validator = SyncValidator()
print("Sync validator initialized")

