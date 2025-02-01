
class ClientOnboardingManager:
    _SECURE_INPUT_TIMEOUT = 300
    async def handle_registration(self, update, context):
        chat_id = update.effective_chat.id
        await context.bot.send_message(
            chat_id=chat_id,
            text='?? *Secure API Key Registration*\n1. Generate Binance Testnet API keys\n'
                 '2. Reply with /api_encrypted [KEY] [SECRET]\n'
                 '*Note:* Keys auto-expire in 5 minutes',
            parse_mode='Markdown'
        )
        try:
            encrypted_data = await self._wait_for_secure_input(chat_id)
            if self._validate_testnet_keys(encrypted_data):
                await self._store_credentials(chat_id, encrypted_data)
        except TimeoutError:
            await context.bot.send_message(chat_id, '? Registration timed out')

