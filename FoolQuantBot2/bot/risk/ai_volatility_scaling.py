import numpy as np

class AIVolatilityScaler:
    def __init__(self):
        self.base_leverage = 5

    def adjust_leverage(self, volatility, sentiment, trend_strength):
        leverage = self.base_leverage * (1 + (sentiment * 0.5) + (trend_strength * 0.3) - (volatility * 0.4))
        return np.clip(leverage, 2, 10)  # Keeps leverage within 2x - 10x range
