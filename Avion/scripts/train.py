import asyncio
import argparse
from avion.ai.training.trainer import ModelTrainer
from avion.utils.logger import Logger

logger = Logger()

async def train_model(model_name: str, epochs: int = 100):
    logger.info(f"Starting training for {model_name}")
    
    try:
        trainer = ModelTrainer(model_name)
        trainer.config['epochs'] = epochs
        
        # Initialize model (placeholder)
        model = None  # Would be your actual model initialization
        
        # Start training
        await trainer.train(model)
        
        logger.info(f"Training completed for {model_name}")
        
    except Exception as e:
        logger.error(f"Training failed: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Train AVION models')
    parser.add_argument('--model', type=str, required=True, help='Model name to train')
    parser.add_argument('--epochs', type=int, default=100, help='Number of epochs')
    
    args = parser.parse_args()
    
    asyncio.run(train_model(args.model, args.epochs))

if __name__ == '__main__':
    main() 