from bot.telegram.telegram_commands import TelegramNotifier

class PaymentClassifier:
    def __init__(self):
        self.notifier = TelegramNotifier()

    def classify_transaction(self, amount):
        if amount % 10 == 0:  # Assuming fixed client payment amounts
            self.notifier.notify_admin(f'Client Payment Detected: {amount} USDT')
            self._process_client_payment(amount)
        else:
            self.notifier.notify_admin(f'Admin Fund Addition Detected: {amount} USDT')

    def _process_client_payment(self, amount):
        # Implement logic to map payment to correct client
        pass
