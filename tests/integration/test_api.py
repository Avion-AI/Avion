import pytest
import aiohttp
import json
from avion.core.config import settings

class TestAPI:
    @pytest.mark.asyncio
    async def test_generate_endpoint(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{settings.api_base_url}/api/generate",
                json={
                    "concept": "Cyber Wolf",
                    "style": "3d"
                }
            ) as response:
                assert response.status == 200
                data = await response.json()
                assert 'name' in data
                assert 'ticker' in data
                assert 'description' in data
                assert 'image_url' in data

    @pytest.mark.asyncio
    async def test_analyze_endpoint(self):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{settings.api_base_url}/api/analyze",
                json={
                    "concept": "Cyber Wolf"
                }
            ) as response:
                assert response.status == 200
                data = await response.json()
                assert 'trend_score' in data
                assert 'sentiment' in data
                assert 'market_cap_estimate' in data 