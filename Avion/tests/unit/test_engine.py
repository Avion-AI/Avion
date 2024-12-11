import pytest
from unittest.mock import Mock, patch
from avion.core.engine import AVIONEngine
from avion.utils.logger import Logger

@pytest.fixture
def engine():
    return AVIONEngine()

@pytest.fixture
def mock_logger():
    with patch('avion.core.engine.Logger') as mock:
        yield mock

class TestAVIONEngine:
    async def test_generate_token(self, engine, mock_logger):
        # Test data
        concept = "Cyber Wolf"
        style = "3d"
        
        # Mock market data
        mock_market_data = {
            'trend_score': 0.85,
            'sentiment': 'bullish',
            'market_cap_estimate': 1000000
        }
        
        # Mock token data
        mock_token_data = {
            'name': 'CyberWolf',
            'ticker': 'CWOLF',
            'description': 'Test description',
            'image_prompt': 'Test prompt'
        }
        
        # Mock image data
        mock_image_data = {
            'url': 'https://test.com/image.png',
            'style': '3d'
        }
        
        # Setup mocks
        engine.market.analyze_concept = Mock(return_value=mock_market_data)
        engine.claude.process_concept = Mock(return_value=mock_token_data)
        engine.leonardo.generate_image = Mock(return_value=mock_image_data)
        
        # Execute
        result = await engine.generate_token(concept, style)
        
        # Assert
        assert result['name'] == 'CyberWolf'
        assert result['ticker'] == 'CWOLF'
        assert result['image_url'] == 'https://test.com/image.png'
        
        # Verify calls
        engine.market.analyze_concept.assert_called_once_with(concept)
        engine.claude.process_concept.assert_called_once()
        engine.leonardo.generate_image.assert_called_once()

    def test_default_config(self, engine):
        config = engine._default_config()
        assert config['optimization_level'] == 'high'
        assert config['market_analysis'] is True
        assert config['concurrent_requests'] == 100
        assert config['image_resolution'] == '4k' 