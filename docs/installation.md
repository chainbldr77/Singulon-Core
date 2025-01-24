# Installation Guide

## Requirements
- Python 3.8+ (with pip)
- Solana CLI (optional if you're deploying the on-chain program)
- Anchor CLI (for building the Rust program)

## Steps
1. Clone the Repo:
   ```bash
   git clone https://github.com/<Your-Dev-Name>/Singulon-Core.git
2. Install Dependencies:
   ```bash
   pip install -r requirements.txt
3. Update the `config/config.json` file with your wallet address and other info.
4. Start the Node:
   ```bash
   python src/main.py
