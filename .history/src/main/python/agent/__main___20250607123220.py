def main():
    import sys, json

    def handle_request(request):
        tool_name = request["tool_use"]["name"]
        args = request["tool_use"].get("arguments", {})
        return {
            "tool_result": {
                "name": tool_name,
                "result": f"Received tool '{tool_name}' with arguments: {args}"
            }
        }

    for line in sys.stdin:
        try:
            request = json.loads(line)
            response = handle_request(request)
            print(json.dumps(response))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()