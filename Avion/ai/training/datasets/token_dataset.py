from typing import List, Dict, Any
import json
import os
from ....utils.logger import Logger

class TokenDataset:
    def __init__(self, data_path: str = 'data/tokens'):
        self.logger = Logger()
        self.data_path = data_path
        self.samples = self._load_samples()
        
    def _load_samples(self) -> List[Dict[str, Any]]:
        """Load training samples from JSON files"""
        samples = []
        try:
            for file in os.listdir(self.data_path):
                if file.endswith('.json'):
                    with open(os.path.join(self.data_path, file), 'r') as f:
                        samples.extend(json.load(f))
        except Exception as e:
            self.logger.error(f"Error loading dataset: {e}")
            return []
            
        self.logger.info(f"Loaded {len(samples)} training samples")
        return samples
    
    def get_batch(self, batch_size: int = 32) -> List[Dict[str, Any]]:
        """Get a random batch of samples"""
        import random
        return random.sample(self.samples, min(batch_size, len(self.samples)))

    def add_sample(self, sample: Dict[str, Any]):
        """Add new training sample"""
        self.samples.append(sample)
        self._save_samples()

    def _save_samples(self):
        """Save samples back to JSON"""
        try:
            os.makedirs(self.data_path, exist_ok=True)
            with open(os.path.join(self.data_path, 'samples.json'), 'w') as f:
                json.dump(self.samples, f)
        except Exception as e:
            self.logger.error(f"Error saving dataset: {e}") 