-- SQL Query Builder for Testing
-- This file contains sample queries for testing database operations

-- Select all test records
SELECT * FROM test_records 
WHERE created_at > DATE('now', '-7 days')
ORDER BY created_at DESC;

-- Count records by status
SELECT status, COUNT(*) as count
FROM test_records
GROUP BY status;

-- Update record status
UPDATE test_records
SET status = 'completed', updated_at = CURRENT_TIMESTAMP
WHERE id = ?;

-- Insert new test record
INSERT INTO test_records (name, status, created_at)
VALUES ('Test Record', 'pending', CURRENT_TIMESTAMP);

