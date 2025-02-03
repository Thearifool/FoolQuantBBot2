# ✅ Secure Audit Logging for Transactions with Profit Tracking
import json

class AuditLogger:
    def log_transaction(self, txn_id, status, details, client_percentage):
        with open("logs/payment_audit.json", "a") as f:
            json.dump({"txn_id": txn_id, "status": status, "details": details, "client_percentage": client_percentage}, f)
            f.write("\n")
