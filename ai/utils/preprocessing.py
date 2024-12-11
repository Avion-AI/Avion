from typing import Dict, Any
from ...utils.logger import Logger

class TextPreprocessor:
    def __init__(self):
        self.logger = Logger()
        self.max_length = 1000
        self.stop_words = {'a', 'an', 'the', 'and', 'or', 'but'}

    def preprocess_text(self, text: str) -> str:
        self.logger.debug(f"Preprocessing text: {text[:50]}...")
        
        # Basic preprocessing
        text = text.lower().strip()
        
        # Remove stop words
        words = text.split()
        words = [w for w in words if w not in self.stop_words]
        
        # Truncate if too long
        if len(words) > self.max_length:
            self.logger.warning(f"Truncating text from {len(words)} to {self.max_length} words")
            words = words[:self.max_length]
        
        return ' '.join(words)

    def clean_prompt(self, prompt: str) -> str:
        # Remove special characters
        cleaned = ''.join(c for c in prompt if c.isalnum() or c.isspace())
        # Remove extra spaces
        cleaned = ' '.join(cleaned.split())
        return cleaned 