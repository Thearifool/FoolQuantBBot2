import time
from binance.client import Client
from bot.api.api_manager import APIManager
from bot.payments.payment_classifier import PaymentClassifier

class FundingWalletMonitor:
    def __init__(self):
        self.client = APIManager().get_admin_client()
        self.classifier = PaymentClassifier()
        self.last_balance = None

    def detect_funding_change(self):
        balance = self.client.get_asset_balance(asset='USDT', wallet='FUNDING')
        if self.last_balance is not None and float(balance['free']) > float(self.last_balance):
            self.classifier.classify_transaction(float(balance['free']) - float(self.last_balance))
        self.last_balance = balance['free']

    def start_monitoring(self):
        while True:
            self.detect_funding_change()
            time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    monitor = FundingWalletMonitor()
    monitor.start_monitoring()
