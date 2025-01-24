import pytest
from src.utils.solana_interaction import SolanaInteraction

def test_get_balance(monkeypatch):
    # Mock the RPC call
    class MockClient:
        def get_balance(self, addr):
            return {"result": {"value": 1234567}}

    def mock_init(self, rpc_url):
        self.client = MockClient()

    monkeypatch.setattr(SolanaInteraction, "__init__", mock_init)

    sol = SolanaInteraction("https://api.mainnet-beta.solana.com")
    balance = sol.get_balance("TestWallet")
    assert balance == 1234567
