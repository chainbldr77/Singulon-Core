from nacl.signing import SigningKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError

class CryptographyUtils:

    @staticmethod
    def generate_keypair():
        """Generates an Ed25519 keypair for Solana or message signing."""
        private_key = SigningKey.generate()
        public_key = private_key.verify_key
        return (private_key, public_key)

    @staticmethod
    def sign_message(private_key, message: str) -> str:
        """Signs a message (str) with the given private key (SigningKey). Returns hex signature."""
        signature = private_key.sign(message.encode("utf-8"))
        return signature.signature.hex()

    @staticmethod
    def verify_signature(public_key, message: str, signature_hex: str) -> bool:
        try:
            signature_bytes = bytes.fromhex(signature_hex)
            public_key.verify(
                message.encode("utf-8"),
                signature_bytes
            )
            return True
        except BadSignatureError:
            return False
