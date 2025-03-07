import json
import os
from typing import Any, Dict, List

import httpx
from mcp.server.fastmcp import FastMCP

CAIYUN_API_KEY = os.environ.get("CAIYUN_API_KEY")
assert CAIYUN_API_KEY, "Please set the CAIYUN_API_KEY environment variable"


def get_weather_alerts(longitude: float, latitude: float) -> List[Dict[str, Any]]:
    url = f"https://api.caiyunapp.com/v2.6/{CAIYUN_API_KEY}/{longitude},{latitude}/weather?alert=true"

    with httpx.Client(timeout=5.0) as client:
        response = client.get(url)
        response.raise_for_status()

        data = response.json()
        # Extract alert information from the response
        alerts = data.get("result", {}).get("alert", {}).get("content", [])

    return alerts


def get_realtime_weather(longitude: float, latitude: float) -> Dict[str, Any]:
    url = f"https://api.caiyunapp.com/v2.6/{CAIYUN_API_KEY}/{longitude},{latitude}/realtime"

    with httpx.Client(timeout=5.0) as client:
        response = client.get(url)
        response.raise_for_status()

        data = response.json()
        # Extract realtime weather information from the response
        realtime_data = data.get("result", {}).get("realtime", {})

    return realtime_data


mcp = FastMCP("CaiyunWeather")


@mcp.tool()
def get_weather_alerts_tool(longitude: float, latitude: float):
    """Fetches weather alerts from Caiyun Weather API v2.6.

    Args:
        longitude: The longitude coordinate of the location.
        latitude: The latitude coordinate of the location.

    Returns:
        A list of dictionaries containing weather alert information. Each dictionary
        contains details about a specific alert. Empty list if no alerts exist or if
        the API response doesn't contain alert data.
    """
    try:
        alerts = get_weather_alerts(longitude, latitude)
    except Exception:
        return "Failed to fetch weather alerts"
    return f"```json\n{json.dumps(alerts, ensure_ascii=False)}\n```"


@mcp.tool()
def get_realtime_weather_tool(longitude: float, latitude: float):
    """Fetches realtime weather information from Caiyun Weather API v2.6.

    Args:
        longitude: The longitude coordinate of the location.
        latitude: The latitude coordinate of the location.

    Returns:
        A dictionary containing realtime weather information. Empty dictionary if no
        realtime data is available or if the API response doesn't contain realtime data.
    """
    try:
        realtime_data = get_realtime_weather(longitude, latitude)
    except Exception:
        return "Failed to fetch realtime"
    return f"```json\n{json.dumps(realtime_data, ensure_ascii=False)}\n```"


if __name__ == "__main__":
    mcp.run(transport="stdio")
