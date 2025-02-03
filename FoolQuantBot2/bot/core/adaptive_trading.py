from bot.api.api_manager import APIManager

class AdaptiveTrading:
    def __init__(self):
        self.api_manager = APIManager()

    def execute_trade(self, trade_details):
        trading_mode = self.api_manager.get_trading_mode()

        if trading_mode == "live":
            self.execute_live_trade(trade_details)
        else:
            self.execute_paper_trade(trade_details)

    def execute_live_trade(self, trade_details):
        # Execute real trade
        print("🔹 Executing live trade:", trade_details)

    def execute_paper_trade(self, trade_details):
        # Execute paper trade
        print("📄 Simulating paper trade:", trade_details)
