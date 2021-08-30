# Polygon API Data
import os
import requests
import pandas as pd

# Get historical financials
class Financials:
  def __init__(self, ticker):
    self.ticker = ticker.upper()
    self.api_key = os.environ['polygon_api_key']

    self.financials = self.get_financials()


  def get_financials(self):
    url = "https://api.polygon.io/v2/reference/financials/{}?type=Y&sort=reportPeriod&apiKey={}".format(self.ticker, self.api_key)

    response = requests.get(url)
    content = response.json()['results']

    df = pd.json_normalize(content).T
    df.columns = df.loc['reportPeriod']
    df.drop('reportPeriod', axis = 0, inplace = True)

    return df
