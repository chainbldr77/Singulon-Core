import numpy as np

class TrendPredictor:
    def predict_trend(self, onchain_data, sentiment_data):
        """
        Basic logic: combine on-chain volume and sentiment scores
        to produce a bullish/bearish indicator.
        """
        volume = onchain_data.get('volume', 0)
        sentiment_score = sentiment_data.get('score', 0)
        # Weighted sum approach (toy logic):
        trend_val = (0.7 * volume) + (0.3 * sentiment_score)
        if trend_val > 5000:
            return "Bullish"
        else:
            return "Bearish"
