import numpy as np

class RiskManager:
    def __init__(self, max_drawdown=0.2, stop_loss_buffer=0.01):
        self.max_drawdown = max_drawdown
        self.stop_loss_buffer = stop_loss_buffer
        self.trade_history = []

    def calculate_position_size(self, balance, risk_factor):
        return balance * min(0.02, risk_factor)

    def update_trade_history(self, trade):
        self.trade_history.append(trade)
        if len(self.trade_history) > 50:
            self.trade_history.pop(0)

    def check_drawdown(self):
        if len(self.trade_history) < 10:
            return False
        max_loss = min([trade["profit"] for trade in self.trade_history])
        return abs(max_loss) >= self.max_drawdown

    def get_stop_loss(self, current_price):
        return current_price * (1 - self.stop_loss_buffer)
