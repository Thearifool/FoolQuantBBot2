# ✅ Updated Payment Classification Logic (Validated)
class PaymentClassifier:
    def classify_payment(self, amount_received, expected_amount, client_percentage):
        expected_due = expected_amount * (client_percentage / 100)
        if amount_received == expected_due:
            return "full"
        elif amount_received > expected_due:
            return "excess"
        else:
            return "partial"