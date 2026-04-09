"""Entry point for running MCP server as a module.

Usage:
    python -m lz_browser_agent.mcp
"""

import asyncio

from lz_browser_agent.mcp.server import main

if __name__ == '__main__':
	asyncio.run(main())
