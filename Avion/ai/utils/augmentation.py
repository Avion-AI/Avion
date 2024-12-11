import random
from typing import List, Dict, Any
from ...utils.logger import Logger

class PromptAugmenter:
    def __init__(self):
        self.logger = Logger()
        self.style_modifiers = {
            '3d': [
                'ultra realistic 3D render',
                'octane render',
                'unreal engine 5',
                'ray tracing',
                'volumetric lighting'
            ],
            'anime': [
                'anime style',
                'manga art',
                'studio ghibli',
                'cel shaded',
                'japanese animation'
            ],
            'minimalist': [
                'minimal design',
                'clean lines',
                'simple shapes',
                'negative space',
                'geometric'
            ]
        }
        
        self.quality_modifiers = [
            'high detail',
            '8k resolution',
            'sharp focus',
            'professional lighting',
            'masterpiece'
        ]

    def augment_prompt(self, prompt: str, style: str, quality_level: str = 'high') -> str:
        self.logger.info(f"Augmenting prompt for style: {style}")
        
        # Get style-specific modifiers
        style_mods = self.style_modifiers.get(style, [])
        
        # Select random modifiers
        selected_style_mods = random.sample(style_mods, min(2, len(style_mods)))
        selected_quality_mods = random.sample(self.quality_modifiers, 2)
        
        # Combine prompt with modifiers
        augmented = f"{prompt}, {', '.join(selected_style_mods)}"
        if quality_level == 'high':
            augmented += f", {', '.join(selected_quality_mods)}"
        
        return augmented

    def generate_variations(self, prompt: str, style: str, count: int = 3) -> List[str]:
        variations = []
        for _ in range(count):
            variations.append(self.augment_prompt(prompt, style))
        return variations 