from mcp.server.fastmcp import FastMCP

mcp = FastMCP("starter-server")


@mcp.tool()
def hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"


@mcp.resource("info://server")
def server_info() -> str:
    """Get server information."""
    return "MCP Starter Server v1.0.0"


@mcp.prompt()
def greeting_prompt(name: str) -> str:
    """Generate a greeting prompt."""
    return f"Please greet {name} warmly and ask how their day is going."


if __name__ == "__main__":
    mcp.run(transport="sse")
