import ccxt
class MultiExchangeExecutor:
    def __init__(self):
        self.exchanges = {
            "binance": ccxt.pro.binance({"enableRateLimit": True}),
            "okx": ccxt.pro.okx({"enableRateLimit": True}),
            "bybit": ccxt.pro.bybit({"enableRateLimit": True})
        }
        self.active_exchange = "binance"
        self.fallback_order = ["okx", "bybit"]

    async def execute_order(self, symbol, side, amount):
        for exchange in [self.active_exchange] + self.fallback_order:
            try:
                return await self.exchanges[exchange].create_order(
                    symbol, 'market', side, amount,
                    params={'test': True}  # Ensures mock trading
                )
            except ccxt.RateLimitExceeded:
                self._rotate_exchange()
