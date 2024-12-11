from typing import Dict, Any
import torch
from ..utils.logger import Logger
from .datasets.token_dataset import TokenDataset
from .weights.model_weights import ModelWeights

class ModelTrainer:
    def __init__(self, model_name: str):
        self.logger = Logger()
        self.model_name = model_name
        self.dataset = TokenDataset()
        self.weights = ModelWeights(model_name)
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        
        # Training config
        self.config = {
            'batch_size': 32,
            'epochs': 100,
            'learning_rate': 1e-4,
            'checkpoint_interval': 10
        }

    async def train(self, model: torch.nn.Module):
        """Train the model"""
        self.logger.info(f"Starting training for {self.model_name}")
        
        model = model.to(self.device)
        optimizer = torch.optim.Adam(model.parameters(), lr=self.config['learning_rate'])
        
        for epoch in range(self.config['epochs']):
            model.train()
            total_loss = 0
            
            # Get training batch
            batch = self.dataset.get_batch(self.config['batch_size'])
            
            for sample in batch:
                optimizer.zero_grad()
                
                # Forward pass
                outputs = model(sample['input'])
                loss = self._compute_loss(outputs, sample['target'])
                
                # Backward pass
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
            
            avg_loss = total_loss / len(batch)
            self.logger.info(f"Epoch {epoch}: Loss = {avg_loss:.4f}")
            
            # Save checkpoint
            if epoch % self.config['checkpoint_interval'] == 0:
                self._save_checkpoint(model, epoch, avg_loss)

    def _compute_loss(self, outputs: torch.Tensor, targets: torch.Tensor) -> torch.Tensor:
        """Compute training loss"""
        criterion = torch.nn.MSELoss()
        return criterion(outputs, targets)

    def _save_checkpoint(self, model: torch.nn.Module, epoch: int, loss: float):
        """Save training checkpoint"""
        checkpoint = {
            'epoch': epoch,
            'model_state': model.state_dict(),
            'loss': loss
        }
        self.weights.save_weights(checkpoint) 