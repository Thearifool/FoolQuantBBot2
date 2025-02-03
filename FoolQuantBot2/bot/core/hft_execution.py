from bot.api.api_manager import APIManager

class HFTExecution:
    def __init__(self):
        self.admin_client = APIManager().get_admin_client()
        self.client_apis = APIManager().client_api_keys

    def execute_admin_trade(self, symbol, side, quantity):
        order = self.admin_client.create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        self._mirror_trade_to_clients(order)

    def _mirror_trade_to_clients(self, admin_order):
        for client_id, client in self.client_apis.items():
            client.create_order(
                symbol=admin_order['symbol'],
                side=admin_order['side'],
                type='MARKET',
                quantity=admin_order['executedQty']
            )
