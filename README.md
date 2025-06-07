# MCP Agent Demo

**MCP Agent Demo** is a simple Python project designed to simulate a basic [Model Customization Protocol (MCP)](https://github.com/github/llm-plugins/blob/main/docs/mcp.md) agent.  
It reads `tool_use` JSON requests from `stdin` and responds with `tool_result` via `stdout`, as expected by tools like Claude Desktop or GitHub Copilot using MCP plugins.

---

## 📁 Project Structure

```
mcp-agent-demo/
├── pyproject.toml
├── README.md
├── src/
│   └── main/
│       └── python/
│           └── mcpagent/
│               ├── __init__.py
│               ├── __main__.py
│               └── core.py
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourname/mcp-agent-demo.git
cd mcp-agent-demo
```

### 2. Install dependencies with Poetry

```bash
poetry install
```

> ⚠️ Requires Python ≥ 3.10 and [Poetry](https://python-poetry.org/) installed (`pip install poetry`)

---

## ▶️ Usage

### Interactive mode

```bash
poetry run agent
```

Then type a valid MCP JSON request, e.g.:

```json
{"tool_use": {"name": "hello", "arguments": {"foo": "bar"}}}
```

Press Enter to see the response.

---

### One-shot command test

```bash
echo '{"tool_use": {"name": "hello", "arguments": {"foo": "bar"}}}' | poetry run agent
```

---

## 🐳 Docker Support

### Build the Docker image

```bash
docker build -t mcp-agent-demo .
```

### Run a test via Docker

```bash
echo '{"tool_use": {"name": "docker_test"}}' | docker run -i --rm mcp-agent-demo
```

---

## 🧪 Example

Input:
```json
{"tool_use": {"name": "hello", "arguments": {"foo": "bar"}}}
```

Output:
```json
{
  "tool_result": {
    "name": "hello",
    "result": "Received tool 'hello' with arguments: {'foo': 'bar'}"
  }
}
```

---

## 📦 Recommended Makefile

```makefile
run:
	poetry run agent

test:
	echo '{"tool_use": {"name": "test"}}' | poetry run agent

docker-build:
	docker build -t mcp-agent-demo .

docker-run:
	echo '{"tool_use": {"name": "docker-test"}}' | docker run -i --rm mcp-agent-demo
```

---

## 📚 Useful Links

- [GitHub MCP Protocol Spec](https://github.com/github/llm-plugins/blob/main/docs/mcp.md)
- [Claude Desktop + MCP Plugin Support](https://www.anthropic.com/news/claude-desktop)