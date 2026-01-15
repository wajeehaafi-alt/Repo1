-- Analytics queries for workflow performance and insights
-- Useful for monitoring and optimization

-- Performance metrics over time
SELECT 
    DATE_TRUNC('hour', started_at) as hour,
    COUNT(*) as execution_count,
    AVG(files_count) as avg_files,
    AVG(EXTRACT(EPOCH FROM (completed_at - started_at))) as avg_duration_seconds,
    COUNT(CASE WHEN status = 'success' THEN 1 END) as success_count,
    COUNT(CASE WHEN status = 'failed' THEN 1 END) as failed_count
FROM workflow_executions
WHERE started_at > NOW() - INTERVAL '7 days'
GROUP BY DATE_TRUNC('hour', started_at)
ORDER BY hour DESC;

-- Repository sync frequency
SELECT 
    source_repo,
    target_repo,
    COUNT(*) as sync_count,
    SUM(files_count) as total_files,
    AVG(EXTRACT(EPOCH FROM (completed_at - started_at))) as avg_duration
FROM workflow_executions
WHERE started_at > NOW() - INTERVAL '30 days'
GROUP BY source_repo, target_repo
ORDER BY sync_count DESC;

-- Error analysis
SELECT 
    error_message,
    COUNT(*) as occurrence_count,
    MAX(started_at) as last_occurrence
FROM workflow_executions
WHERE status = 'failed'
    AND error_message IS NOT NULL
GROUP BY error_message
ORDER BY occurrence_count DESC
LIMIT 20;

-- File sync success rate by operation type
SELECT 
    operation_type,
    COUNT(*) as total_operations,
    COUNT(CASE WHEN status = 'success' THEN 1 END) as success_count,
    COUNT(CASE WHEN status = 'failed' THEN 1 END) as failed_count,
    ROUND(100.0 * COUNT(CASE WHEN status = 'success' THEN 1 END) / COUNT(*), 2) as success_rate_percent
FROM file_syncs
WHERE synced_at > NOW() - INTERVAL '30 days'
GROUP BY operation_type
ORDER BY total_operations DESC;

-- Pull request metrics
SELECT 
    DATE_TRUNC('day', created_at) as day,
    COUNT(*) as prs_created,
    COUNT(CASE WHEN status = 'merged' THEN 1 END) as prs_merged,
    AVG(EXTRACT(EPOCH FROM (merged_at - created_at))) as avg_time_to_merge_seconds
FROM pull_requests
WHERE created_at > NOW() - INTERVAL '30 days'
GROUP BY DATE_TRUNC('day', created_at)
ORDER BY day DESC;

-- Most synced file types
SELECT 
    SUBSTRING(file_path FROM '\.([^.]+)$') as file_extension,
    COUNT(*) as sync_count,
    COUNT(DISTINCT execution_id) as unique_executions
FROM file_syncs
WHERE synced_at > NOW() - INTERVAL '30 days'
    AND file_path LIKE '%.%'
GROUP BY SUBSTRING(file_path FROM '\.([^.]+)$')
ORDER BY sync_count DESC
LIMIT 20;

-- Workflow execution trends
SELECT 
    workflow_name,
    COUNT(*) as total_executions,
    AVG(files_count) as avg_files_per_execution,
    SUM(files_count) as total_files_synced,
    COUNT(CASE WHEN status = 'success' THEN 1 END) as successful_executions,
    COUNT(CASE WHEN status = 'failed' THEN 1 END) as failed_executions
FROM workflow_executions
WHERE started_at > NOW() - INTERVAL '30 days'
GROUP BY workflow_name
ORDER BY total_executions DESC;

