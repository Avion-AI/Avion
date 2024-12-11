from typing import Dict, Any
from .validators import validate_input
from ..utils.logger import Logger

class TokenProcessor:
    def __init__(self):
        self.logger = Logger()

    async def process_token_request(self, data: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.info("Processing token generation request")
        
        # Validate input data
        validate_input(data)
        
        # Process token parameters
        processed_data = await self._process_parameters(data)
        
        # Apply optimization
        optimized_data = self._optimize_parameters(processed_data)
        
        return optimized_data

    async def _process_parameters(self, data: Dict[str, Any]) -> Dict[str, Any]:
        return {
            'concept': data['concept'].lower().strip(),
            'style': data.get('style', '3d'),
            'optimization_level': data.get('optimization_level', 'high'),
            'market_analysis': data.get('market_analysis', True)
        }

    def _optimize_parameters(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if data['optimization_level'] == 'high':
            data['image_quality'] = 'ultra'
            data['processing_priority'] = 'high'
        return data 