import asyncio
import time
import numpy as np
import ccxt.async_support as ccxt

class HFTExecution:
    def __init__(self, exchange_id="binance", max_slippage=0.1):
        self.exchange = getattr(ccxt, exchange_id)({"enableRateLimit": True})
        self.max_slippage = max_slippage

    async def place_order(self, symbol, side, amount, price=None):
        try:
            if price is None:
                ticker = await self.exchange.fetch_ticker(symbol)
                price = ticker["last"]

            # Validate slippage
            order_book = await self.exchange.fetch_order_book(symbol)
            best_price = order_book["asks"][0][0] if side == "buy" else order_book["bids"][0][0]
            if abs(price - best_price) / best_price > self.max_slippage:
                raise ValueError(f"Slippage too high: {price} vs {best_price}")

            order = await self.exchange.create_order(symbol, "limit", side, amount, price)
            return order
        except Exception as e:
            print(f"[ERROR] HFT Order Failed: {e}")
            return None

    async def monitor_market(self, symbol, strategy):
        while True:
            market_data = await self.exchange.fetch_ticker(symbol)
            decision = strategy.analyze(market_data)
            if decision:
                await self.place_order(symbol, decision["side"], decision["amount"], decision.get("price"))
            await asyncio.sleep(0.5)  # Run at 2Hz frequency
