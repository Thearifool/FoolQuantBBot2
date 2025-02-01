import numpy as np

class MaxDrawdownMonitor:
    def __init__(self, threshold=10):
        self.threshold = threshold
        self.history = []

    def update_pnl(self, pnl):
        self.history.append(pnl)
        drawdown = (np.max(self.history) - pnl) / np.max(self.history) * 100
        return drawdown > self.threshold
