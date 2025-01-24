from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.system_program import transfer, TransferParams
from solana.keypair import Keypair
from base58 import b58decode

class SolanaInteraction:
    def __init__(self, rpc_url):
        self.client = Client(rpc_url)

    def get_balance(self, wallet_address: str) -> int:
        response = self.client.get_balance(wallet_address)
        return response["result"]["value"]

    def send_sol(self, from_private_key: str, to_address: str, lamports: int):
        """Send SOL from one wallet to another."""
        from_keypair = Keypair.from_secret_key(b58decode(from_private_key))
        txn = Transaction().add(
            transfer(
                TransferParams(
                    from_pubkey=from_keypair.public_key,
                    to_pubkey=to_address,
                    lamports=lamports
                )
            )
        )
        result = self.client.send_transaction(txn, from_keypair)
        return result
