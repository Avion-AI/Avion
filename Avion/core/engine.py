from typing import Dict, Any
from ..ai.models.claude import ClaudeProcessor
from ..ai.models.leonardo import ImageGenerator
from ..services.market_analyzer import MarketAnalyzer
from ..utils.logger import Logger

class AVIONEngine:
    def __init__(self, config: Dict[str, Any] = None):
        self.logger = Logger()
        self.claude = ClaudeProcessor()
        self.leonardo = ImageGenerator()
        self.market = MarketAnalyzer()
        self.config = config or self._default_config()

    def _default_config(self) -> Dict[str, Any]:
        return {
            'optimization_level': 'high',
            'market_analysis': True,
            'concurrent_requests': 100,
            'image_resolution': '4k'
        }

    async def generate_token(self, concept: str, style: str) -> Dict[str, Any]:
        self.logger.info(f"Initializing token generation for concept: {concept}")
        
        # Analyze market trends
        market_data = await self.market.analyze_concept(concept)
        
        # Generate token name and description
        token_data = await self.claude.process_concept(
            concept=concept,
            market_data=market_data
        )
        
        # Generate token image
        image_data = await self.leonardo.generate_image(
            prompt=token_data['image_prompt'],
            style=style
        )

        return {
            'name': token_data['name'],
            'ticker': token_data['ticker'],
            'description': token_data['description'],
            'image_url': image_data['url']
        } 