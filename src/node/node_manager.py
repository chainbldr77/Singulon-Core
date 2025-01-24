import json
import os
from utils.solana_interaction import SolanaInteraction
from utils.logger import Logger

class NodeManager:
    def __init__(self, config_path):
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Config file not found: {config_path}")
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.solana = SolanaInteraction(self.config["rpc_url"])

    def start_node(self):
        Logger.log("Starting node with wallet: " + self.config["wallet_address"])
        balance = self.solana.get_balance(self.config["wallet_address"])
        Logger.log(f"Current balance: {balance} lamports")

    def sync(self):
        # In a real scenario, you'd fetch on-chain states or update local states
        Logger.log("Node synchronization complete.")
