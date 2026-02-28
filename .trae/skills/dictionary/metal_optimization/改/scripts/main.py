import sys
import json
import argparse
import traceback
import os
from pathlib import Path

def execute_logic(params):
    """
    Core logic for 改 (Refactor/Modify).
    Supports simple search/replace logic.
    """
    target = params.get("target") or params.get("file_path")
    search_str = params.get("search") or params.get("old_str")
    replace_str = params.get("replace") or params.get("new_str")
    
    if not target:
        raise ValueError("Missing 'target' parameter")
    if search_str is None:
        raise ValueError("Missing 'search' parameter")
    if replace_str is None:
        raise ValueError("Missing 'replace' parameter")

    print(f"Executing 改 (Modify) on: {target}")
    
    file_path = Path(target)
    if not file_path.is_absolute():
        file_path = Path(os.getcwd()) / target
        
    if not file_path.exists():
        return {"status": "error", "message": f"File not found: {file_path}"}
        
    try:
        content = file_path.read_text(encoding='utf-8')
        
        if search_str not in content:
            return {
                "status": "failure",
                "message": "Search string not found in file",
                "target": str(file_path)
            }
            
        new_content = content.replace(search_str, replace_str, 1) # Only replace first occurrence by default for safety
        
        file_path.write_text(new_content, encoding='utf-8')
        
        return {
            "status": "success",
            "message": "File updated successfully",
            "target": str(file_path),
            "changes_made": True
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Modification failed: {str(e)}"
        }

def main():
    parser = argparse.ArgumentParser(description="改: 代码重构与安全加固")
    parser.add_argument('--input', help='JSON input parameters', default='{}')
    args = parser.parse_args()
    
    try:
        params = json.loads(args.input)
        result = execute_logic(params)
        print(json.dumps({"status": "success", "data": result}, ensure_ascii=False, indent=2))
    except Exception as e:
        error_res = {
            "status": "error",
            "message": str(e),
            "traceback": traceback.format_exc()
        }
        print(json.dumps(error_res, ensure_ascii=False))
        sys.exit(1)

if __name__ == "__main__":
    main()
