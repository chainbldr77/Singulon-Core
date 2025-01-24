# API Reference

## Python Modules

### `solana_interaction.py`
- **get_balance(wallet_address)** -> int
- **send_sol(private_key, to_address, amount_lamports)** -> Transaction signature

### `cryptography.py`
- **generate_keypair()** -> (private_key, public_key)
- **sign_message(private_key, message)** -> signature
- **verify_signature(public_key, signature, message)** -> bool

### `equilibrium_model.py`
- **predict_equilibrium(onchain_data)** -> float

### `advanced_transformer.py`
- **deep_insight_analysis(history_data)** -> dict (complex analysis results)

---

## On-Chain Anchor Program

### `initialize`
Initializes the Singulon program account.

### `update_equilibrium`
Updates on-chain record of equilibrium based on AI insights.

