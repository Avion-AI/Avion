# API Configuration
API_VERSION = "v1"
MAX_BATCH_SIZE = 10
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# Image Generation
SUPPORTED_STYLES = [
    '3d',
    'anime',
    'minimalist',
    'cartoon',
    'realistic'
]

IMAGE_SIZES = {
    'standard': '1024x1024',
    'high': '2048x2048',
    'ultra': '4096x4096'
}

# Token Generation
MAX_NAME_LENGTH = 32
MAX_TICKER_LENGTH = 8
MAX_DESCRIPTION_LENGTH = 500

# Rate Limiting
RATE_LIMIT = {
    'requests_per_minute': 60,
    'requests_per_hour': 1000,
    'requests_per_day': 10000
}

# Error Messages
ERROR_MESSAGES = {
    'invalid_input': 'Invalid input parameters provided',
    'rate_limit': 'Rate limit exceeded. Please try again later',
    'api_error': 'Error communicating with external API',
    'validation_error': 'Validation failed for provided data',
    'auth_error': 'Authentication failed. Please check your API key'
}

# Market Analysis
MARKET_THRESHOLDS = {
    'trend_score': 0.8,
    'sentiment_score': 0.6,
    'volatility_threshold': 0.4
}

# Cache Settings
CACHE_CONFIG = {
    'max_size': 1000,
    'ttl': 3600,  # 1 hour
    'refresh_interval': 300  # 5 minutes
}

# Security
SECURITY_CONFIG = {
    'min_key_length': 32,
    'hash_algorithm': 'sha256',
    'token_expiry': 3600,  # 1 hour
    'required_headers': [
        'X-API-Key',
        'X-Request-ID',
        'X-Signature'
    ]
} 