import sys
import json
import argparse
import traceback
import subprocess
import os
from pathlib import Path

def execute_logic(params):
    """
    Core logic for 判 (Judge/Analyze).
    Can run linters, static analysis, or simply inspect file stats.
    For this implementation, we'll support a simple 'file_info' mode and a 'python_syntax_check' mode.
    """
    target = params.get("target") or params.get("path")
    mode = params.get("mode") or "file_info"

    if not target:
        raise ValueError("Missing 'target' parameter")

    print(f"Executing 判 (Judge) on: {target} in mode: {mode}")
    
    file_path = Path(target)
    if not file_path.is_absolute():
        file_path = Path(os.getcwd()) / target
        
    if not file_path.exists():
        return {"status": "error", "message": f"Path not found: {file_path}"}
        
    if mode == "file_info":
        stat = file_path.stat()
        return {
            "status": "success",
            "type": "directory" if file_path.is_dir() else "file",
            "size": stat.st_size,
            "modified": stat.st_mtime,
            "extension": file_path.suffix
        }
    
    elif mode == "python_check":
        if not file_path.suffix == ".py":
             return {"status": "error", "message": "Not a python file"}
        
        try:
            # Run basic syntax check using py_compile
            import py_compile
            py_compile.compile(str(file_path), doraise=True)
            return {
                "status": "success", 
                "message": "Syntax OK"
            }
        except py_compile.PyCompileError as e:
             return {
                "status": "failure",
                "message": f"Syntax Error: {e.msg}",
                "details": str(e)
            }
        except Exception as e:
             return {"status": "error", "message": str(e)}

    return {
        "status": "error",
        "message": f"Unknown mode: {mode}"
    }

def main():
    parser = argparse.ArgumentParser(description="判: 错误诊断与代码分析")
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
