import requests

class MacroEconomicMonitor:
    def __init__(self):
        self.api_url = 'https://api.stlouisfed.org/fred/series/observations'

    def fetch_cpi_data(self):
        response = requests.get(self.api_url, params={'series_id': 'CPIAUCSL'})
        return response.json()['observations']
