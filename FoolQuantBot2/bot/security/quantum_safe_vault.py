from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

class QuantumSafeVault:
    def __init__(self):
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=64,
            iterations=600000,
            salt=os.urandom(32)
        )
        self.hmac_key = os.urandom(32)

    def sign_request(self, request):
        h = hmac.HMAC(self.hmac_key, hashes.SHA512())
        h.update(request.encode())
        return h.finalize()

    def verify_request(self, request, signature):
        h = hmac.HMAC(self.hmac_key, hashes.SHA512())
        h.update(request.encode())
        try:
            h.verify(signature)
            return True
        except:
            return False
