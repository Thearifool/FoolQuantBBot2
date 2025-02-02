class TieredMFAPolicy:
    def __init__(self):
        self.tiers = {'low': 0, 'mid': 10000, 'high': 50000}

    def enforce_mfa(self, client):
        return client.balance >= self.tiers['high']
