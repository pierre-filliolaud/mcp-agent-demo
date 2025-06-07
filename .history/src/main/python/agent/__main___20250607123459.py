import sys
import json

def main():
    for line in sys.stdin:
        try:
            request = json.loads(line)
            tool_name = request["tool_use"]["name"]
            args = request["tool_use"].get("arguments", {})
            result = {
                "tool_result": {
                    "name": tool_name,
                    "result": f"Received tool '{tool_name}' with arguments: {args}"
                }
            }
            print(json.dumps(result))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()