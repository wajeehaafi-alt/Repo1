# Implementation Guide

## Quick Start

This guide will help you quickly set up and start using the bi-directional GitHub repository sync workflow.

## Prerequisites Checklist

- [ ] n8n instance running (self-hosted or cloud)
- [ ] GitHub Personal Access Tokens for each account
- [ ] Access to source and target repositories
- [ ] Proper permissions on repositories (read/write)

## Step-by-Step Setup

### 1. Prepare GitHub Credentials

Create Personal Access Tokens with the following scopes:
- `repo` (Full control of private repositories)
- `workflow` (Update GitHub Action workflows)

Store tokens securely in n8n credentials:
- **Header Auth Account 4**: For Ramzanx0553 repositories
- **Header Auth Account 5**: For wajeehaafi-alt repositories

### 2. Import Workflow

1. Open n8n workflow editor
2. Click "Import from File"
3. Select `WORKFLOW_FIXED_COMPLETE.json`
4. Verify all nodes are properly connected

### 3. Configure Credentials

**Important**: Update credentials for Repo2 → Repo1 route:

These nodes need **Account 5** (for wajeehaafi-alt/Repo1):
- Get SHA5
- Create Branch5
- Check If File Exists5
- Update Existing File5
- Create New File5
- Create PR5

These nodes should use **Account 4** (for Ramzanx0553/Repo2):
- Get Commit Details5
- Get File Content5

### 4. Test the Workflow

1. Create 2-3 test files in source repository
2. Commit and push:
   ```bash
   git add .
   git commit -m "Test sync"
   git push origin main
   ```
3. Check n8n execution logs
4. Verify PR created in target repository
5. Confirm all files appear in PR

## Common Configuration Issues

### Issue: Validation Failed
- **Cause**: Missing or incorrect Accept header
- **Fix**: Ensure Accept header is `application/vnd.github.v3+json`

### Issue: Authentication Error
- **Cause**: Wrong credentials for repository
- **Fix**: Use Account 5 for wajeehaafi-alt repos, Account 4 for Ramzanx0553 repos

### Issue: PR Only Shows One File
- **Cause**: Aggregate node not collecting all items
- **Fix**: Verify `keepOnlySet: false` in Aggregate nodes

### Issue: toNumber() Error
- **Cause**: Type mismatch in If File Exists condition
- **Fix**: Use `String($json.status || $json.statusCode || 404).toNumber()`

## Best Practices

1. **Start Small**: Test with 2-3 files before syncing many
2. **Monitor Logs**: Regularly check n8n execution logs
3. **Review PRs**: Always review synced files before merging
4. **Secure Tokens**: Rotate GitHub tokens every 90 days
5. **Backup Workflow**: Export workflow JSON regularly

## Troubleshooting

### Workflow Not Triggering
- Check webhook is configured in GitHub
- Verify webhook URL is accessible
- Check n8n is running and active

### Files Not Appearing in PR
- Verify all files are committed to same branch
- Check Aggregate node configuration
- Ensure Create PR runs after all files processed

### Rate Limiting Errors
- Reduce sync frequency
- Implement exponential backoff
- Use GitHub App instead of PAT for higher limits

## Support Resources

- n8n Documentation: https://docs.n8n.io
- GitHub API Documentation: https://docs.github.com/en/rest
- Workflow JSON: `WORKFLOW_FIXED_COMPLETE.json`

