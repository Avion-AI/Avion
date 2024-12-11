from typing import Dict, Any
from ..utils.logger import Logger

class ValidationError(Exception):
    pass

def validate_input(data: Dict[str, Any]) -> bool:
    logger = Logger()
    
    required_fields = ['concept']
    valid_styles = ['3d', 'anime', 'minimalist', 'cartoon', 'realistic']
    
    # Check required fields
    for field in required_fields:
        if field not in data:
            logger.error(f"Missing required field: {field}")
            raise ValidationError(f"Missing required field: {field}")
    
    # Validate style if provided
    if 'style' in data and data['style'] not in valid_styles:
        logger.error(f"Invalid style: {data['style']}")
        raise ValidationError(f"Invalid style. Must be one of: {valid_styles}")
    
    return True

def validate_output(data: Dict[str, Any]) -> bool:
    required_fields = ['name', 'ticker', 'description', 'image_url']
    
    for field in required_fields:
        if field not in data:
            raise ValidationError(f"Missing required output field: {field}")
    
    return True 