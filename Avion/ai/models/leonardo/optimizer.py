from typing import Dict, Any
from ....utils.logger import Logger
from ....core.config import IMAGE_SIZES

class ImageOptimizer:
    def __init__(self):
        self.logger = Logger()
        self.supported_sizes = IMAGE_SIZES
        self.quality_presets = {
            'standard': {'sharpness': 0.5, 'contrast': 0.5, 'saturation': 0.5},
            'high': {'sharpness': 0.7, 'contrast': 0.6, 'saturation': 0.6},
            'ultra': {'sharpness': 0.9, 'contrast': 0.8, 'saturation': 0.7}
        }

    async def optimize_image(self, image_data: Dict[str, Any], quality: str = 'high') -> Dict[str, Any]:
        self.logger.info(f"Optimizing image with {quality} quality preset")
        
        # Apply quality presets
        optimized = await self._apply_quality_settings(image_data, quality)
        
        # Optimize resolution
        optimized = await self._optimize_resolution(optimized, quality)
        
        # Format optimization
        optimized = self._optimize_format(optimized)
        
        return optimized

    async def _apply_quality_settings(self, image_data: Dict[str, Any], quality: str) -> Dict[str, Any]:
        settings = self.quality_presets.get(quality, self.quality_presets['standard'])
        image_data.update({
            'optimization_settings': settings,
            'quality_preset': quality
        })
        return image_data

    async def _optimize_resolution(self, image_data: Dict[str, Any], quality: str) -> Dict[str, Any]:
        target_size = self.supported_sizes.get(quality, self.supported_sizes['standard'])
        image_data['target_resolution'] = target_size
        return image_data

    def _optimize_format(self, image_data: Dict[str, Any]) -> Dict[str, Any]:
        image_data['format'] = 'png'  # Always use PNG for highest quality
        image_data['compression'] = 'lossless'
        return image_data 