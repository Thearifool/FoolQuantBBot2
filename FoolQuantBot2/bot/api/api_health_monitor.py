import time
import requests

class PreemptiveAPIMonitor:
    def __init__(self):
        self.endpoints = {
            'binance': 'https://api.binance.com/api/v3/ping',
            'okx': 'https://www.okx.com/api/v5/public/time'
        }

    def health_check(self):
        for name, url in self.endpoints.items():
            start = time.monotonic()
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    print(f'{name} OK in {time.monotonic() - start:.2f}ms')
                    return True
            except:
                print(f'{name} failed')
        return False
