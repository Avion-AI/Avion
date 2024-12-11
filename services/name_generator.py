import asyncio
from typing import Dict, Any, List
from ..utils.logger import Logger

class NameGenerator:
    def __init__(self):
        self.logger = Logger()
        self.name_patterns = {
            'tech': ['Cyber', 'Quantum', 'Neural', 'Digital', 'Tech'],
            'nature': ['Solar', 'Luna', 'Terra', 'Stellar', 'Nova'],
            'power': ['Alpha', 'Omega', 'Prime', 'Ultra', 'Meta'],
            'crypto': ['Chain', 'Block', 'Token', 'Coin', 'Crypto']
        }
        self.suffixes = ['AI', 'X', 'Protocol', 'Network', 'DAO']

    async def generate_name(self, concept: str, market_data: Dict[str, Any]) -> Dict[str, Any]:
        self.logger.info(f"Generating name for concept: {concept}")
        
        # Analyze concept category
        category = await self._analyze_category(concept)
        
        # Generate base name
        base_name = await self._generate_base_name(concept, category)
        
        # Apply market trends
        if market_data['trend_score'] > 0.8:
            base_name = self._apply_trend_modifier(base_name)
        
        # Generate variations
        variations = self._generate_variations(base_name)
        
        return {
            'name': base_name,
            'variations': variations,
            'category': category
        }

    async def _analyze_category(self, concept: str) -> str:
        # Simulate category analysis
        await asyncio.sleep(0.5)
        for category, patterns in self.name_patterns.items():
            if any(pattern.lower() in concept.lower() for pattern in patterns):
                return category
        return 'tech'  # Default category

    async def _generate_base_name(self, concept: str, category: str) -> str:
        words = concept.split()
        if len(words) > 2:
            words = words[:2]
        
        # Add category-specific prefix if needed
        if not any(pattern.lower() in concept.lower() 
                  for pattern in self.name_patterns[category]):
            prefix = self.name_patterns[category][0]
            words.insert(0, prefix)
        
        return ''.join(word.capitalize() for word in words)

    def _apply_trend_modifier(self, name: str) -> str:
        if len(name) < 15:  # Only add suffix if name isn't too long
            return f"{name}{self.suffixes[0]}"
        return name

    def _generate_variations(self, base_name: str) -> List[str]:
        variations = []
        for suffix in self.suffixes:
            if len(base_name) + len(suffix) <= 20:
                variations.append(f"{base_name}{suffix}")
        return variations 