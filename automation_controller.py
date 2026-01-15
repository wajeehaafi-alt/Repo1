#!/usr/bin/env python3
"""
Automation Controller
Main controller for workflow automation system
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class SyncTask:
    source_repo: str
    target_repo: str
    files: list
    status: str = "pending"
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

class AutomationController:
    def __init__(self):
        self.tasks = []
        self.is_running = False
    
    def add_task(self, task: SyncTask):
        """Add a new sync task"""
        self.tasks.append(task)
        return task
    
    def get_task_status(self, task_id: int) -> Optional[SyncTask]:
        """Get status of a specific task"""
        if 0 <= task_id < len(self.tasks):
            return self.tasks[task_id]
        return None
    
    def start(self):
        """Start the automation controller"""
        self.is_running = True
        print("Automation controller started")
    
    def stop(self):
        """Stop the automation controller"""
        self.is_running = False
        print("Automation controller stopped")

controller = AutomationController()
print("Automation controller initialized")

