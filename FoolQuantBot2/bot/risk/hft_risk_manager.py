import numpy as np

class HFTRiskManager:
    def __init__(self, max_drawdown=10, stop_loss=1.5, take_profit=3.0):
        self.max_drawdown = max_drawdown
        self.stop_loss = stop_loss
        self.take_profit = take_profit

    def calculate_risk(self, symbol, atr):
        return {
            "stop_loss": atr * self.stop_loss,
            "take_profit": atr * self.take_profit
        }

    def check_drawdown(self, pnl_history):
        drawdown = np.min(pnl_history) / np.max(pnl_history) * 100
        return drawdown > self.max_drawdown
