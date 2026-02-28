import sys
import json
import argparse
import traceback
import subprocess
import os
import platform

def execute_logic(params):
    """
    Core logic for 管 (Manage/Execute).
    Executes shell commands safely.
    """
    command = params.get("command") or params.get("cmd")
    cwd = params.get("cwd") or os.getcwd()
    
    if not command:
        raise ValueError("Missing 'command' parameter")

    print(f"Executing 管 (Manage): '{command}' in {cwd}")
    
    try:
        # Determine shell based on OS
        shell = True
        executable = None
        if platform.system() == "Windows":
             executable = "powershell" # Prefer PowerShell on Windows
        
        # Execute command
        result = subprocess.run(
            command, 
            cwd=cwd, 
            shell=shell, 
            executable=executable,
            capture_output=True, 
            text=True,
            timeout=60 # 60s timeout for safety
        )
        
        return {
            "status": "success" if result.returncode == 0 else "failure",
            "return_code": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "command": command
        }
    except subprocess.TimeoutExpired:
         return {
            "status": "timeout",
            "message": "Command execution timed out (60s)",
            "command": command
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Execution failed: {str(e)}",
            "command": command
        }

def main():
    parser = argparse.ArgumentParser(description="管: 依赖管理与环境配置")
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
