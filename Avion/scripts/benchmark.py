import asyncio
import time
import argparse
from avion.core.engine import AVIONEngine
from avion.utils.logger import Logger

logger = Logger()

async def run_benchmark(iterations: int = 100):
    """Run performance benchmark"""
    logger.info(f"Starting benchmark with {iterations} iterations")
    
    engine = AVIONEngine()
    total_time = 0
    successful = 0
    
    for i in range(iterations):
        start_time = time.time()
        try:
            await engine.generate_token(
                concept="Benchmark Test",
                style="3d"
            )
            successful += 1
        except Exception as e:
            logger.error(f"Iteration {i} failed: {e}")
        finally:
            total_time += time.time() - start_time
    
    avg_time = total_time / iterations
    success_rate = (successful / iterations) * 100
    
    logger.info(f"Benchmark Results:")
    logger.info(f"Average Time: {avg_time:.2f}s")
    logger.info(f"Success Rate: {success_rate:.1f}%")
    logger.info(f"Total Time: {total_time:.2f}s")

def main():
    parser = argparse.ArgumentParser(description='Run AVION benchmarks')
    parser.add_argument('--iterations', type=int, default=100,
                      help='Number of iterations to run')
    
    args = parser.parse_args()
    asyncio.run(run_benchmark(args.iterations))

if __name__ == '__main__':
    main() 