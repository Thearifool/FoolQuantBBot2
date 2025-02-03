# ✅ Ensure Clients Follow Admin's Trading Mode
class AdaptiveTrading:
    def sync_trading_mode(self, admin_mode):
        for client in self.clients:
            client.set_trading_mode(admin_mode)
