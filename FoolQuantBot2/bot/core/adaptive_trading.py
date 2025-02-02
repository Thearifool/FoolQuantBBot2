import numpy as np
from bot.macro.macro_economic_monitor import MacroEconomicMonitor

class AdaptiveTradingEngine:
    def __init__(self):
        self.position_cap = 0.15
        self.macro_monitor = MacroEconomicMonitor()

    def calculate_position(self, sentiment, macro_risk):
        raw_size = sentiment * macro_risk * 100
        return min(raw_size, self.position_cap)

    async def execute_trade(self, exchange, size):
        return await exchange.create_order(
            symbol='BTC/USDT',
            type='limit',
            side='buy' if sentiment > 0 else 'sell',
            amount=size
        )
