import sys
import json
import argparse
import traceback
import subprocess

def execute_logic(params):
    """
    Core logic for 搜 (Search).
    Uses DuckDuckGo Search via subprocess call or direct integration.
    Since we are in a Python script, we can simulate the tool behavior or call the actual tool if available.
    For this "Dictionary Skill", we will act as a proxy to the `duckduckgo-search` skill or perform search directly if library is installed.
    
    Given the constraint that this is a standalone script, we'll try to use a simple search library or mock it for now, 
    but ideally it should call the 'WebSearch' capability of the agent.
    
    HOWEVER, since this script is run BY the agent, the agent should read the output.
    But to make this script *useful*, it should probably perform the search itself.
    
    Let's assume `duckduckgo_search` package is available or we use `requests` to hit a search API.
    For robustness in this environment, we will output a structured instruction for the Agent to execute the search,
    OR we try to import `duckduckgo_search`.
    """
    query = params.get("query") or params.get("q")
    if not query:
        raise ValueError("Missing 'query' parameter")

    print(f"Executing 搜 (Search) for: {query}")
    
    results = []
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            # Get first 5 results
            results = list(ddgs.text(query, max_results=5))
    except ImportError:
        return {
            "status": "partial_success",
            "message": "duckduckgo_search library not found. Please install it or use the Agent's built-in WebSearch tool.",
            "instruction": f"Agent, please execute WebSearch for: '{query}'",
            "query": query
        }
    except Exception as e:
         return {
            "status": "error",
            "message": f"Search failed: {str(e)}",
            "query": query
        }

    return {
        "message": f"Successfully executed 搜 for '{query}'",
        "results": results
    }

def main():
    parser = argparse.ArgumentParser(description="搜: 网络与文档搜索技能")
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
