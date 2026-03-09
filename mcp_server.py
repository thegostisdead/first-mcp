from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("superapi")


API_BASE = "http://localhost:8000"


async def make_request(url: str) -> dict[str, Any] | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


@mcp.tool()
async def get_uuid() -> str:
    """Generate a uuid v4

    """
    url = f"{API_BASE}/generate/uuid4"
    data = await make_request(url)

    if not data or "result" not in data:
        return "Unable to generate a uuid"

    return data["result"]

@mcp.tool()
async def compute_hash(data: str) -> str:
    """Compute hash in md5 format for a given text data.

    Args:
        data: str the text to be hashed
    """
    url = f"{API_BASE}/hash/md5?data={data}"
    data = await make_request(url)

    if not data or "result" not in data:
        return "Unable to compute hash"

    return data["result"]

@mcp.tool()
async def add(left: int, right: int) -> str:
    """Compute a add operation on two intergers.

    Args:
        left: int
        right: int
    """
    url = f"{API_BASE}/add?left={left}&right={right}"
    data = await make_request(url)

    if not data or "result" not in data:
        return "Unable to compute add"

    return str(data["result"])

def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()