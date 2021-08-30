# Polygon API Data
import pandas as pd
import requests

from config import polygon_api_key


# Get historical financials
class Financials:
    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self.api_key = polygon_api_key

    def get_financials(self):
        url = "https://api.polygon.io/v2/reference/financials/{}?type=Y&sort=-reportPeriod&apiKey={}"\
          .format(self.ticker, self.api_key)

        response = requests.get(url)
        content = response.json()['results']

        df = pd.json_normalize(content).T
        df.columns = df.loc['reportPeriod']
        df.drop('reportPeriod', axis=0, inplace=True)

        return df
