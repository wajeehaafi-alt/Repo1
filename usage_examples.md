# Usage Examples

## Overview
This document provides practical examples of using the bi-directional GitHub repository sync workflow.

## Example 1: Basic File Sync

### Scenario
Sync a single file from Repo-A to Repo-B.

### Steps
1. Create or modify a file in Repo-A
2. Commit the changes:
   ```bash
   git add file.py
   git commit -m "Update file.py"
   git push origin main
   ```
3. The workflow automatically:
   - Detects the push event
   - Creates a branch in Repo-B
   - Creates a PR with the file

### Expected Result
- PR created in Repo-B
- File appears in the PR
- PR can be merged to sync the file

## Example 2: Multiple Files Sync

### Scenario
Sync 5 files in a single commit.

### Steps
1. Create multiple files:
   ```bash
   touch file1.py file2.js file3.html file4.css file5.md
   ```
2. Commit all files:
   ```bash
   git add .
   git commit -m "Add multiple files"
   git push origin main
   ```
3. The workflow processes all files sequentially

### Expected Result
- All 5 files appear in the PR
- PR shows "Files changed: 5"
- All files can be merged together

## Example 3: File Update Sync

### Scenario
Update an existing file that was previously synced.

### Steps
1. Modify the file in source repository
2. Commit and push:
   ```bash
   git add file.py
   git commit -m "Update file.py"
   git push origin main
   ```
3. The workflow detects the file exists and updates it

### Expected Result
- File is updated in target repository
- PR shows the changes as modifications
- SHA is correctly updated

## Example 4: Large File Sync

### Scenario
Sync a large file (>1MB).

### Steps
1. Create a large file (e.g., 2MB)
2. Commit and push
3. Monitor the workflow execution

### Expected Result
- Large file is synced successfully
- PR shows the file
- File integrity is maintained

## Troubleshooting Examples

### Issue: PR only shows one file
**Solution**: Check that Aggregate nodes have `keepOnlySet: false`

### Issue: Validation Failed error
**Solution**: Verify Accept header is set to `application/vnd.github.v3+json`

### Issue: Wrong credentials error
**Solution**: Ensure correct GitHub account credentials are used for each repository

## Best Practices

1. **Test with small batches first**: Start with 2-3 files before syncing many
2. **Monitor execution logs**: Check n8n execution logs for any errors
3. **Review PRs before merging**: Always review synced files before merging
4. **Use descriptive commit messages**: Helps track what was synced
5. **Keep credentials secure**: Rotate GitHub tokens periodically

