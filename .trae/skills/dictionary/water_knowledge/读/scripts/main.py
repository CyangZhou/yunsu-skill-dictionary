import sys
import json
import argparse
import traceback
import os
import requests
from pathlib import Path

def execute_logic(params):
    """
    Core logic for 读 (Read).
    Supports reading local files or fetching URL content.
    """
    target = params.get("target") or params.get("path") or params.get("url")
    if not target:
        raise ValueError("Missing 'target' (path or url) parameter")

    print(f"Executing 读 (Read) for: {target}")
    
    # Check if URL
    if target.startswith("http://") or target.startswith("https://"):
        try:
            response = requests.get(target, timeout=10)
            response.raise_for_status()
            content = response.text
            # Simple text extraction (mock)
            # In a real scenario, use BeautifulSoup or similar
            return {
                "type": "url",
                "source": target,
                "content_preview": content[:1000] + "..." if len(content) > 1000 else content,
                "length": len(content)
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to fetch URL: {str(e)}"
            }
    
    # Assume Local File
    file_path = Path(target)
    if not file_path.is_absolute():
        # Try to resolve relative to current working directory
        file_path = Path(os.getcwd()) / target
    
    if file_path.exists() and file_path.is_file():
        try:
            content = file_path.read_text(encoding='utf-8', errors='replace')
            return {
                "type": "file",
                "source": str(file_path),
                "content": content,
                "lines": len(content.splitlines())
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"Failed to read file: {str(e)}"
            }
    else:
        return {
            "status": "error",
            "message": f"File not found: {target}"
        }

def main():
    parser = argparse.ArgumentParser(description="读: 文件读取与网页抓取")
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
