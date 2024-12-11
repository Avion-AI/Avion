import hashlib
import hmac
import os
from typing import Dict, Any
from .logger import Logger

class SecurityManager:
    def __init__(self):
        self.logger = Logger()
        self._secret_key = self._load_secret_key()

    def _load_secret_key(self) -> str:
        key = os.getenv('AVION_SECRET_KEY')
        if not key:
            self.logger.warning("No secret key found, generating new one")
            key = self._generate_secret_key()
        return key

    def _generate_secret_key(self) -> str:
        return hashlib.sha256(os.urandom(32)).hexdigest()

    def validate_request(self, data: Dict[str, Any], signature: str) -> bool:
        computed_signature = self._compute_signature(data)
        return hmac.compare_digest(computed_signature, signature)

    def _compute_signature(self, data: Dict[str, Any]) -> str:
        message = ''.join(f"{k}={v}" for k, v in sorted(data.items()))
        return hmac.new(
            self._secret_key.encode(),
            message.encode(),
            hashlib.sha256
        ).hexdigest()

    def encrypt_sensitive_data(self, data: str) -> str:
        # Implement encryption logic here
        return f"encrypted_{data}"

    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        # Implement decryption logic here
        return encrypted_data.replace("encrypted_", "") 