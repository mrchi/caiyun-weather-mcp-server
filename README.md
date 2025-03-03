# Caiyun Weather MCP Server

An MCP server that provides seamless access to the Caiyun Weather API.

## Quick Start

1. **Register and Obtain API Key**:  
   Visit [Caiyun Platform](https://platform.caiyunapp.com/login) to register and generate your API key.

2. **Clone the Repository and Set Up Environment**:  
   Clone the repository and use `uv` to create a Python virtual environment and install dependencies.

   ```bash
   git clone https://github.com/mrchi/caiyun-weather-mcp-server.git
   cd caiyun-weather-mcp-server/
   uv venv
   uv sync
   ```

3. **Configure Environment Variables**:  
   Create a `.env` file to store your API key.

   ```
   CAIYUN_API_KEY="your-key"
   ```

4. **Configure MCP Client**:  
   Open an MCP-compatible client, such as [Claude for Desktop](https://claude.ai/download) or [Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) in VSCode, and configure it as follows:

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

5. **Query the Weather**:  
   Simply ask:  

   ```
   How about the weather in Tiananmen Square?
   ```
