import pytest
import os
from avion.utils.logger import Logger

@pytest.fixture(autouse=True)
def setup_test_env():
    """Setup test environment variables"""
    os.environ['AVION_ENV'] = 'test'
    os.environ['LEONARDO_API_KEY'] = 'test_key'
    os.environ['CLAUDE_API_KEY'] = 'test_key'
    
@pytest.fixture
def logger():
    """Provide test logger"""
    return Logger() 