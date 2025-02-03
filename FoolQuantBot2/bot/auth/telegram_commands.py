# ✅ Updated Telegram Invoice Structure (Confidential Format)
import logging

def send_invoice(client_id, amount_due, profit_earned, payment_status):
    categories = {
        "AI Token Cost": amount_due * 0.33,
        "Quant API Cost": amount_due * 0.30,
        "Security & Compliance": amount_due * 0.37
    }

    message = f"📜 *Invoice for Client {client_id}*\n"
    message += f"📆 *Billing Period:* (Auto-filled)\n"
    message += f"💰 *Profit Earned:* ${profit_earned:.2f}\n"
    message += f"💳 *Total Fee Due:* ${amount_due:.2f}\n\n"
    
    message += "🔹 *Breakdown of Charges:*\n"
    for category, cost in categories.items():
        message += f"- {category}: ${cost:.2f}\n"

    message += f"\n✅ *Payment Status:* {payment_status}\n"
    message += "⚠ *Note:* Please complete the payment before the due date to continue trading.\n"
    message += "🔗 *Payment Method:* Send to Binance ID: **XXXXXXX** (Funding Wallet)."

    logging.info(f"Invoice Sent: {client_id}")
    return message
