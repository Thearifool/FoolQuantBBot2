# ✅ Auto-Detection of Funding Wallet Transactions with Classification
import time

class FundingWalletMonitor:
    def check_for_payments(self):
        new_payments = self._get_wallet_transactions()
        for txn in new_payments:
            classification = PaymentClassifier().classify_payment(txn.amount, txn.expected, txn.client_percentage)
            if classification == "full":
                self._confirm_payment(txn)
            elif classification == "partial":
                self._notify_partial_payment(txn)
            elif classification == "excess":
                self._handle_overpayment(txn)
