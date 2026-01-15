-- Database queries for workflow system
-- Common queries for monitoring and reporting

-- Get all workflow executions
SELECT 
    id,
    workflow_name,
    source_repo,
    target_repo,
    status,
    files_count,
    started_at,
    completed_at,
    EXTRACT(EPOCH FROM (completed_at - started_at)) as duration_seconds
FROM workflow_executions
ORDER BY started_at DESC
LIMIT 100;

-- Get execution statistics by status
SELECT 
    status,
    COUNT(*) as count,
    AVG(files_count) as avg_files,
    AVG(EXTRACT(EPOCH FROM (completed_at - started_at))) as avg_duration_seconds
FROM workflow_executions
WHERE started_at > NOW() - INTERVAL '30 days'
GROUP BY status;

-- Get failed executions with error messages
SELECT 
    id,
    workflow_name,
    source_repo,
    target_repo,
    error_message,
    started_at
FROM workflow_executions
WHERE status = 'failed'
ORDER BY started_at DESC;

-- Get file sync statistics
SELECT 
    operation_type,
    status,
    COUNT(*) as count,
    COUNT(CASE WHEN status = 'success' THEN 1 END) as success_count,
    COUNT(CASE WHEN status = 'failed' THEN 1 END) as failed_count
FROM file_syncs
WHERE synced_at > NOW() - INTERVAL '7 days'
GROUP BY operation_type, status;

-- Get pull request statistics
SELECT 
    status,
    COUNT(*) as pr_count,
    AVG(EXTRACT(EPOCH FROM (merged_at - created_at))) as avg_time_to_merge_seconds
FROM pull_requests
WHERE created_at > NOW() - INTERVAL '30 days'
GROUP BY status;

-- Get most active repositories
SELECT 
    source_repo,
    COUNT(*) as sync_count,
    SUM(files_count) as total_files_synced
FROM workflow_executions
WHERE started_at > NOW() - INTERVAL '30 days'
GROUP BY source_repo
ORDER BY sync_count DESC
LIMIT 10;

-- Get recent file syncs with details
SELECT 
    fs.id,
    fs.file_path,
    fs.operation_type,
    fs.status,
    fs.synced_at,
    we.workflow_name,
    we.source_repo,
    we.target_repo
FROM file_syncs fs
JOIN workflow_executions we ON fs.execution_id = we.id
WHERE fs.synced_at > NOW() - INTERVAL '24 hours'
ORDER BY fs.synced_at DESC;

