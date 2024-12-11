import os
import argparse
import subprocess
from avion.utils.logger import Logger

logger = Logger()

def deploy(environment: str):
    """Deploy AVION to specified environment"""
    logger.info(f"Deploying to {environment}")
    
    # Environment-specific configurations
    configs = {
        'development': {
            'url': 'http://localhost:8000',
            'env_file': '.env.development'
        },
        'staging': {
            'url': 'https://staging.avion.ai',
            'env_file': '.env.staging'
        },
        'production': {
            'url': 'https://api.avion.ai',
            'env_file': '.env.production'
        }
    }
    
    if environment not in configs:
        raise ValueError(f"Invalid environment: {environment}")
    
    config = configs[environment]
    
    try:
        # Load environment variables
        if os.path.exists(config['env_file']):
            logger.info(f"Loading environment from {config['env_file']}")
            subprocess.run(f"source {config['env_file']}", shell=True)
        
        # Run deployment steps
        steps = [
            "pip install -r requirements.txt",
            "python -m pytest tests/",
            f"uvicorn server:app --host 0.0.0.0 --port {os.getenv('PORT', '8000')}"
        ]
        
        for step in steps:
            logger.info(f"Running: {step}")
            subprocess.run(step, shell=True, check=True)
            
        logger.info(f"Deployment successful! API available at {config['url']}")
        
    except subprocess.CalledProcessError as e:
        logger.error(f"Deployment failed: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Deploy AVION')
    parser.add_argument('--env', type=str, default='development',
                      choices=['development', 'staging', 'production'],
                      help='Deployment environment')
    
    args = parser.parse_args()
    deploy(args.env)

if __name__ == '__main__':
    main() 