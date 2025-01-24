from utils.logger import Logger
from src.models.equilibrium_model import EquilibriumModel
from src.models.trend_predictor import TrendPredictor
from src.models.advanced_transformer import AdvancedTransformer
import numpy as np

class NodeBrain:
    """
    Central AI Brain that orchestrates data gathering, AI inference,
    and node actions.
    """

    def __init__(self, node_manager):
        self.node_manager = node_manager
        self.equilibrium_model = EquilibriumModel()
        self.trend_predictor = TrendPredictor()
        self.advanced_transformer = AdvancedTransformer()

        # Potentially load pre-trained weights or historical data
        Logger.log("NodeBrain AI modules initialized.")

    def gather_data(self):
        Logger.log("Gathering on-chain and external data.")
        # Placeholder: real logic would fetch from Solana & oracles
        self.onchain_data = {"volume": 6000}
        self.sentiment_data = {"score": 3.8}
        self.historical_data = np.random.rand(10, 24, 8)

    def execute_ai_pipelines(self):
        # LSTM or model-based equilibrium
        eq_prediction = self.equilibrium_model.predict_equilibrium(
            np.random.rand(1, 24, 8)
        )
        # Basic trend
        trend = self.trend_predictor.predict_trend(self.onchain_data, self.sentiment_data)
        # Transformer-based deep analysis
        transformer_out = self.advanced_transformer(self.historical_data)

        Logger.log(f"Equilibrium Model Output: {eq_prediction}")
        Logger.log(f"Trend Predictor Output: {trend}")
        Logger.log(f"Advanced Transformer Output: {transformer_out.numpy()}")

    def perform_governance_actions(self):
        # Potential logic for governance or liquidity rebalancing
        Logger.log("Performing governance actions (placeholder).")
        self.node_manager.sync()
