
.PHONY: api install

api:
	uv run fastapi dev api.py

install:
	claude mcp add superapi uv run $(CURDIR)/mcp_server.py
