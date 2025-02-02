from bot.api.api_manager import APIManager

# Initialize components
api_manager = APIManager()
auth = TwoFactorAuth()
audit_logger = AuditLogger()

async def switch_live_trading(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not auth.is_admin(user_id):
        await update.message.reply_text("❌ You are not authorized to change trading mode.")
        return

    if await auth.request_2fa(user_id):
        await update.message.reply_text("⏳ Switching to live trading in 30 seconds...")
        time.sleep(30)

        api_manager.set_trading_mode("live")
        audit_logger.log_event("Admin switched to LIVE trading mode.")

        await update.message.reply_text("✅ Live trading activated!")
    else:
        await update.message.reply_text("❌ 2FA verification failed. Trading mode unchanged.")

async def switch_paper_trading(update: Update, context: CallbackContext):
    user_id = update.effective_user.id
    if not auth.is_admin(user_id):
        await update.message.reply_text("❌ You are not authorized to change trading mode.")
        return

    api_manager.set_trading_mode("paper")
    audit_logger.log_event("Admin switched to PAPER trading mode.")

    await update.message.reply_text("✅ Paper trading activated!")

async def show_status(update: Update, context: CallbackContext):
    trading_mode = api_manager.get_trading_mode()
    await update.message.reply_text(f"📌 **Current Trading Mode:** {trading_mode.upper()}")

register_handlers(application)
application.add_handler(CommandHandler("live", switch_live_trading))
application.add_handler(CommandHandler("paper", switch_paper_trading))
application.add_handler(CommandHandler("status", show_status))
