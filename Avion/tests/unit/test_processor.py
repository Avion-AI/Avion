import pytest
from unittest.mock import Mock, patch
from avion.core.processor import TokenProcessor
from avion.core.validators import ValidationError

@pytest.fixture
def processor():
    return TokenProcessor()

class TestTokenProcessor:
    @pytest.mark.asyncio
    async def test_process_token_request_valid(self, processor):
        # Test data
        input_data = {
            'concept': 'Cyber Wolf',
            'style': '3d',
            'optimization_level': 'high'
        }
        
        # Process request
        result = await processor.process_token_request(input_data)
        
        # Assert
        assert result['concept'] == 'cyber wolf'
        assert result['style'] == '3d'
        assert result['optimization_level'] == 'high'
        assert result['market_analysis'] is True
        
    @pytest.mark.asyncio
    async def test_process_token_request_invalid(self, processor):
        # Test data without required field
        input_data = {
            'style': '3d'
        }
        
        # Assert raises validation error
        with pytest.raises(ValidationError):
            await processor.process_token_request(input_data)
            
    def test_optimize_parameters_high(self, processor):
        data = {
            'optimization_level': 'high',
            'concept': 'test'
        }
        
        result = processor._optimize_parameters(data)
        assert result['image_quality'] == 'ultra'
        assert result['processing_priority'] == 'high' 