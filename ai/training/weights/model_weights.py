import os
from typing import Dict, Any
import torch
from ....utils.logger import Logger

class ModelWeights:
    def __init__(self, model_name: str):
        self.logger = Logger()
        self.model_name = model_name
        self.weights_dir = 'weights'
        self.weights_path = os.path.join(self.weights_dir, f"{model_name}.pth")

    def save_weights(self, state_dict: Dict[str, Any]):
        """Save model weights to file"""
        try:
            os.makedirs(self.weights_dir, exist_ok=True)
            torch.save(state_dict, self.weights_path)
            self.logger.info(f"Saved weights for {self.model_name}")
        except Exception as e:
            self.logger.error(f"Error saving weights: {e}")

    def load_weights(self) -> Dict[str, Any]:
        """Load model weights from file"""
        try:
            if os.path.exists(self.weights_path):
                weights = torch.load(self.weights_path)
                self.logger.info(f"Loaded weights for {self.model_name}")
                return weights
        except Exception as e:
            self.logger.error(f"Error loading weights: {e}")
        
        return None

    def get_latest_checkpoint(self) -> str:
        """Get path to latest checkpoint"""
        checkpoints = []
        checkpoint_dir = os.path.join(self.weights_dir, 'checkpoints')
        
        if os.path.exists(checkpoint_dir):
            checkpoints = [f for f in os.listdir(checkpoint_dir) 
                         if f.startswith(self.model_name)]
            
        return os.path.join(checkpoint_dir, sorted(checkpoints)[-1]) if checkpoints else None 