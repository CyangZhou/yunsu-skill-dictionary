import sys
import json
import argparse
import traceback
import os
from pathlib import Path

def execute_logic(params):
    """
    Core logic for 写 (Write).
    Writes content to a file.
    """
    file_path = params.get("path") or params.get("file_path")
    content = params.get("content")
    
    if not file_path:
        raise ValueError("Missing 'path' parameter")
    if content is None:
        raise ValueError("Missing 'content' parameter")

    print(f"Executing 写 (Write) to: {file_path}")
    
    target_path = Path(file_path)
    if not target_path.is_absolute():
        target_path = Path(os.getcwd()) / file_path
        
    try:
        # Create directories if they don't exist
        target_path.parent.mkdir(parents=True, exist_ok=True)
        
        target_path.write_text(content, encoding='utf-8')
        
        return {
            "status": "success",
            "message": f"Successfully wrote to {target_path}",
            "bytes_written": len(content.encode('utf-8'))
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Failed to write file: {str(e)}"
        }

def main():
    parser = argparse.ArgumentParser(description="写: 文件写入与代码生成")
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
