-- Database Schema Design for Workflow System
-- Creates tables for tracking sync operations

-- Workflow execution log
CREATE TABLE IF NOT EXISTS workflow_executions (
    id SERIAL PRIMARY KEY,
    workflow_name VARCHAR(255) NOT NULL,
    source_repo VARCHAR(255),
    target_repo VARCHAR(255),
    branch_name VARCHAR(255),
    commit_sha VARCHAR(40),
    status VARCHAR(50) DEFAULT 'pending',
    files_count INTEGER DEFAULT 0,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    error_message TEXT
);

-- File sync tracking
CREATE TABLE IF NOT EXISTS file_syncs (
    id SERIAL PRIMARY KEY,
    execution_id INTEGER REFERENCES workflow_executions(id),
    file_path VARCHAR(500) NOT NULL,
    file_sha VARCHAR(40),
    operation_type VARCHAR(20), -- 'create', 'update', 'delete'
    status VARCHAR(50) DEFAULT 'pending',
    synced_at TIMESTAMP,
    error_message TEXT
);

-- Pull request tracking
CREATE TABLE IF NOT EXISTS pull_requests (
    id SERIAL PRIMARY KEY,
    execution_id INTEGER REFERENCES workflow_executions(id),
    pr_number INTEGER,
    pr_url VARCHAR(500),
    title VARCHAR(500),
    status VARCHAR(50) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    merged_at TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX idx_executions_status ON workflow_executions(status);
CREATE INDEX idx_executions_source_repo ON workflow_executions(source_repo);
CREATE INDEX idx_file_syncs_execution ON file_syncs(execution_id);
CREATE INDEX idx_prs_execution ON pull_requests(execution_id);

-- Insert sample data
INSERT INTO workflow_executions (workflow_name, source_repo, target_repo, status)
VALUES ('Repo2 → Repo1', 'Ramzanx0553/Repo2', 'wajeehaafi-alt/Repo1', 'completed');

