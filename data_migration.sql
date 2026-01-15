-- Data Migration Script for Testing
-- Migrates data between repositories

-- Create migration table
CREATE TABLE IF NOT EXISTS migration_log (
    id SERIAL PRIMARY KEY,
    source_repo VARCHAR(255),
    target_repo VARCHAR(255),
    file_count INTEGER,
    migrated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50)
);

-- Insert migration record
INSERT INTO migration_log (source_repo, target_repo, file_count, status)
VALUES ('Repo-A', 'Repo-B', 10, 'completed');

-- Query migration history
SELECT * FROM migration_log
WHERE migrated_at > NOW() - INTERVAL '7 days'
ORDER BY migrated_at DESC;

-- Update migration status
UPDATE migration_log
SET status = 'in_progress'
WHERE id = 1;

