import os
import argparse
from pdoc import pdoc
from avion.utils.logger import Logger

logger = Logger()

def generate_documentation(output_dir: str = 'docs'):
    """Generate API documentation using pdoc"""
    logger.info("Generating documentation...")
    
    try:
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate documentation
        modules = ['avion']
        pdoc(*modules, output_dir=output_dir)
        
        logger.info(f"Documentation generated successfully in {output_dir}")
        
    except Exception as e:
        logger.error(f"Documentation generation failed: {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Generate AVION documentation')
    parser.add_argument('--output', type=str, default='docs',
                      help='Output directory for documentation')
    
    args = parser.parse_args()
    generate_documentation(args.output)

if __name__ == '__main__':
    main() 