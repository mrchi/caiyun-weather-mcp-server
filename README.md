# caiyun-weather-mcp-server

A MCP server that provides access to Caiyun Weather API.

## Quickstart

First, go to https://platform.caiyunapp.com/login to register and create an API KEY.

Clone repo, use `uv` to create python virtual environment, and install requirements

```
git clone https://github.com/mrchi/caiyun-weather-mcp-server.git
cd caiyun-weather-mcp-server/
uv venv
uv sync
```

Create a environment variable file to save the API KEY, such as `.env`. 

```
CAIYUN_API_KEY="your-key"
```

Open your client that supports MCP, such as [Claude for Desktop](https://claude.ai/download) or [Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) in VSCode. Config like this:

```json
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "env": {},
            "args": [
                "--directory",
                "<your repo directory>",
                "run",
                "--env-file",
                ".env",
                "servers/caiyun_weather.py"
            ]
        }
    }
}
```

Just ask: 

```
how about the weather in Tiananmen Square?
```
