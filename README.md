# MCP Server (Python)

A starter MCP (Model Context Protocol) server built with Python and FastMCP.

## Local Development

```bash
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m src.server
```

## Included Examples

- **Tool**: `hello` — Say hello to someone
- **Resource**: `info://server` — Get server info
- **Prompt**: `greeting_prompt` — Generate a greeting

## Adding Tools

Edit `src/server.py` to add new tools, resources, and prompts:

```python
@mcp.tool()
def my_tool(param: str) -> str:
    """Description of what this tool does."""
    return f"Result: {param}"
```

## Deploy on StackBlaze

This template includes a `stackblaze.yaml` for deploying the MCP server with SSE transport.
