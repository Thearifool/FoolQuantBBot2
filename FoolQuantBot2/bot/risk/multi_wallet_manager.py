class MultiWalletManager:
    def __init__(self, wallets):
        self.wallets = wallets

    def allocate_risk(self, client_balance):
        total_balance = sum(wallet.balance for wallet in self.wallets)
        for wallet in self.wallets:
            wallet.risk_limit = min(wallet.balance / total_balance * client_balance, wallet.balance * 0.25)
