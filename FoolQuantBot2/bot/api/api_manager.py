class APIManager:
    def __init__(self):
        self.trading_mode = "paper"

    def set_trading_mode(self, mode):
        if mode in ["live", "paper"]:
            self.trading_mode = mode
            print(f"⚙ Trading mode set to: {mode.upper()}")

    def get_trading_mode(self):
        return self.trading_mode
