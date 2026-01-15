# Integration Guide

## Overview
This guide explains how to integrate the bi-directional GitHub repository sync workflow into your development process.

## Prerequisites

- n8n instance (self-hosted or cloud)
- GitHub accounts with appropriate permissions
- Access to source and target repositories

## Setup Instructions

### Step 1: Configure GitHub Credentials
1. Create GitHub Personal Access Tokens for each account
2. Add tokens to n8n credentials:
   - Header Auth Account 4 For Github (for Ramzanx0553)
   - Header Auth Account 5 For Github (for wajeehaafi-alt)

### Step 2: Import Workflow
1. Open n8n workflow editor
2. Import `WORKFLOW_FIXED_COMPLETE.json`
3. Verify all nodes are connected correctly

### Step 3: Configure Repository Mappings
The workflow supports 6 bidirectional sync routes:
- Repo-A ↔ Repo-B
- Org_Testing_Repo ↔ Per_Testing_Repo
- Repo1 ↔ Repo2

### Step 4: Test the Workflow
1. Create test files in source repository
2. Commit and push changes
3. Verify PR is created in target repository
4. Check that all files appear in the PR

## Troubleshooting

### Common Issues

**Issue**: PR only shows one file
- **Solution**: Ensure Aggregate nodes have `keepOnlySet: false`

**Issue**: Validation Failed error
- **Solution**: Check Accept header is set to `application/vnd.github.v3+json`
- **Solution**: Verify correct GitHub credentials are used for each repository

**Issue**: toNumber() error
- **Solution**: Expression should be `String($json.status || $json.statusCode || 404).toNumber()`

## Best Practices

1. Always test with 2-5 files before using in production
2. Monitor workflow execution logs regularly
3. Keep GitHub tokens secure and rotate periodically
4. Review PRs before merging to ensure correctness

## Support

For issues or questions, refer to the workflow documentation or contact the development team.

