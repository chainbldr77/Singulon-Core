import pytest
from src.models.trend_predictor import TrendPredictor

def test_trend_predictor_bullish():
    predictor = TrendPredictor()
    onchain_data = {"volume": 6000}
    sentiment_data = {"score": 2.0}
    trend = predictor.predict_trend(onchain_data, sentiment_data)
    assert trend == "Bullish"

def test_trend_predictor_bearish():
    predictor = TrendPredictor()
    onchain_data = {"volume": 1000}
    sentiment_data = {"score": 0.5}
    trend = predictor.predict_trend(onchain_data, sentiment_data)
    assert trend == "Bearish"
