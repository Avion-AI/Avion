from typing import Dict, Any
import os

class Settings:
    def __init__(self):
        self.env = os.getenv('AVION_ENV', 'development')
        self.debug = self.env == 'development'
        self.api_version = '1.0.0'
        
        # API Settings
        self.api_base_url = 'https://api.avion.ai'
        self.max_requests_per_minute = 1000
        self.timeout_seconds = 30
        
        # Image Generation Settings
        self.default_image_size = '4096x4096'
        self.supported_styles = ['3d', 'anime', 'minimalist', 'cartoon', 'realistic']
        self.max_prompt_length = 500
        
        # Market Analysis Settings
        self.market_analysis_interval = 300  # 5 minutes
        self.trend_threshold = 0.8
        self.sentiment_threshold = 0.6

    def get_api_config(self) -> Dict[str, Any]:
        return {
            'base_url': self.api_base_url,
            'version': self.api_version,
            'timeout': self.timeout_seconds
        }

    def get_image_config(self) -> Dict[str, Any]:
        return {
            'default_size': self.default_image_size,
            'styles': self.supported_styles,
            'max_prompt_length': self.max_prompt_length
        } 