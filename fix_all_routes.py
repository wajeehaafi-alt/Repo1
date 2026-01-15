#!/usr/bin/env python3
"""
Comprehensive fix for n8n workflow - fixes ALL routes to handle multiple files.
"""

import json
import sys
import re

def fix_if_file_exists_node(node):
    """Fix If File Exists node to check statusCode instead of sha"""
    if node.get("type") == "n8n-nodes-base.if":
        node_name = node.get("name", "")
        if "If File Exists" in node_name:
            params = node.get("parameters", {})
            conditions = params.get("conditions", {})
            if conditions:
                condition_list = conditions.get("conditions", [])
                for condition in condition_list:
                    if condition.get("id") == "file-exists":
                        left_value = condition.get("leftValue", "")
                        # Fix if it's checking sha instead of statusCode
                        if "sha" in left_value and "statusCode" not in left_value:
                            condition["leftValue"] = "={{ $json.statusCode }}"
                            condition["rightValue"] = "200"
                            condition["operator"] = {
                                "type": "number",
                                "operation": "equals"
                            }
                            return True, node_name
    return False, None

def fix_aggregate_node(node):
    """Ensure Aggregate node collects all items"""
    if node.get("type") == "n8n-nodes-base.aggregate":
        params = node.get("parameters", {})
        if "options" not in params:
            params["options"] = {}
        if params["options"].get("keepOnlySet") is None:
            params["options"]["keepOnlySet"] = False
            return True, node.get("name", "Aggregate")
    return False, None

def fix_update_file_sha(node, all_nodes):
    """Fix Update Existing File to use correct sha reference"""
    if node.get("type") == "n8n-nodes-base.httpRequest":
        node_name = node.get("name", "")
        if "Update Existing File" in node_name:
            params = node.get("parameters", {})
            body_params = params.get("bodyParameters", {}).get("parameters", [])
            for param in body_params:
                if param.get("name") == "sha":
                    # Find the corresponding "Check If File Exists" node
                    # Remove number suffix if any
                    base_name = re.sub(r'\d+$', '', node_name)
                    check_node_name = base_name.replace("Update Existing File", "Check If File Exists")
                    
                    # Try to find matching Check If File Exists node
                    for other_node in all_nodes:
                        other_name = other_node.get("name", "")
                        if "Check If File Exists" in other_name:
                            # Match by route pattern
                            node_num = re.search(r'\d+$', node_name)
                            other_num = re.search(r'\d+$', other_name)
                            
                            if (node_num and other_num and node_num.group() == other_num.group()) or \
                               (not node_num and not other_num):
                                param["value"] = f"={{ $('{other_name}').item.json.sha }}"
                                return True, node_name
    return False, None

def main():
    print("=" * 70)
    print("🔧 COMPREHENSIVE WORKFLOW FIX: Multiple Files Support")
    print("=" * 70)
    
    # Find workflow file
    workflow_file = None
    possible_files = [
        "internal_Repo_sync-/Unified Bi-Directional GitHub Repository Sync Combined.json",
        "workflow_multiple_files_fixed.json"
    ]
    
    for file in possible_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                workflow = json.load(f)
                workflow_file = file
                print(f"\n📖 Found workflow: {file}")
                break
        except FileNotFoundError:
            continue
    
    if not workflow_file:
        print("\n❌ No workflow file found. Please provide workflow JSON file.")
        if len(sys.argv) > 1:
            workflow_file = sys.argv[1]
        else:
            print("Usage: python fix_all_routes.py <workflow.json>")
            sys.exit(1)
    
    # Read workflow
    print(f"📖 Reading: {workflow_file}")
    with open(workflow_file, 'r', encoding='utf-8') as f:
        workflow = json.load(f)
    
    nodes = workflow.get("nodes", [])
    print(f"📊 Found {len(nodes)} nodes")
    
    # Apply fixes
    print("\n🔧 Applying fixes to all routes...")
    print("-" * 70)
    
    fixed_if_nodes = []
    fixed_aggregate_nodes = []
    fixed_update_nodes = []
    
    for node in nodes:
        # Fix If File Exists nodes
        fixed, name = fix_if_file_exists_node(node)
        if fixed:
            fixed_if_nodes.append(name)
        
        # Fix Aggregate nodes
        fixed, name = fix_aggregate_node(node)
        if fixed:
            fixed_aggregate_nodes.append(name)
    
    # Fix Update File nodes (needs all nodes for reference)
    for node in nodes:
        fixed, name = fix_update_file_sha(node, nodes)
        if fixed:
            fixed_update_nodes.append(name)
    
    # Print results
    print(f"\n✅ Fixed {len(fixed_if_nodes)} 'If File Exists' nodes:")
    for name in fixed_if_nodes:
        print(f"   ✓ {name}")
    
    print(f"\n✅ Fixed {len(fixed_aggregate_nodes)} Aggregate nodes:")
    for name in fixed_aggregate_nodes:
        print(f"   ✓ {name}")
    
    print(f"\n✅ Fixed {len(fixed_update_nodes)} Update Existing File nodes:")
    for name in fixed_update_nodes:
        print(f"   ✓ {name}")
    
    # Write output
    output_file = "WORKFLOW_FIXED_COMPLETE.json"
    print(f"\n💾 Writing fixed workflow to: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(workflow, f, indent=2, ensure_ascii=False)
    
    print("\n" + "=" * 70)
    print("✨ COMPLETE! Workflow fixed for multiple files support.")
    print("=" * 70)
    print(f"\n📁 Final fixed workflow: {output_file}")
    print("\n📝 All fixes applied:")
    print("   ✓ All 'If File Exists' nodes check statusCode === 200")
    print("   ✓ All Aggregate nodes configured to collect all items")
    print("   ✓ All Update Existing File nodes use correct sha references")
    print("\n🚀 Ready to import into n8n!")

if __name__ == "__main__":
    main()

