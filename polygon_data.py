# Polygon API Data
import pandas as pd
import requests

from config import polygon_api_key


# Get historical financials
class Financials:
    def __init__(self, ticker: str):
        self.ticker = ticker.upper()
        self.api_key = polygon_api_key

        self.metrics = ['calendarDate', 'accumulatedOtherComprehensiveIncome', 'assets', 'assetsAverage',
                        'assetsCurrent', 'assetsNonCurrent', 'assetTurnover', 'bookValuePerShare', 'capitalExpenditure',
                        'cashAndEquivalents', 'cashAndEquivalentsUSD', 'costOfRevenue', 'consolidatedIncome',
                        'currentRatio', 'debtToEquityRatio', 'debt', 'debtCurrent', 'debtNonCurrent', 'debtUSD',
                        'deferredRevenue', 'depreciationAmortizationAndAccretion', 'deposits', 'dividendYield',
                        'dividendsPerBasicCommonShare', 'earningBeforeInterestTaxes',
                        'earningsBeforeInterestTaxesDepreciationAmortization', 'EBITDAMargin',
                        'earningsBeforeInterestTaxesDepreciationAmortizationUSD', 'earningBeforeInterestTaxesUSD',
                        'earningsBeforeTax', 'earningsPerBasicShare', 'earningsPerDilutedShare',
                        'earningsPerBasicShareUSD', 'shareholdersEquity', 'averageEquity', 'shareholdersEquityUSD',
                        'enterpriseValue', 'enterpriseValueOverEBIT', 'enterpriseValueOverEBITDA', 'freeCashFlow',
                        'freeCashFlowPerShare', 'foreignCurrencyUSDExchangeRate', 'grossProfit', 'grossMargin',
                        'goodwillAndIntangibleAssets', 'interestExpense', 'investedCapital', 'investedCapitalAverage',
                        'inventory', 'investments', 'investmentsCurrent', 'investmentsNonCurrent', 'totalLiabilities',
                        'currentLiabilities', 'liabilitiesNonCurrent', 'marketCapitalization', 'netCashFlow',
                        'netCashFlowBusinessAcquisitionsDisposals', 'issuanceEquityShares', 'issuanceDebtSecurities',
                        'paymentDividendsOtherCashDistributions', 'netCashFlowFromFinancing',
                        'netCashFlowFromInvesting', 'netCashFlowInvestmentAcquisitionsDisposals',
                        'netCashFlowFromOperations', 'effectOfExchangeRateChangesOnCash', 'netIncome',
                        'netIncomeCommonStock', 'netIncomeCommonStockUSD', 'netLossIncomeFromDiscontinuedOperations',
                        'netIncomeToNonControllingInterests', 'profitMargin', 'operatingExpenses', 'operatingIncome',
                        'tradeAndNonTradePayables', 'payoutRatio', 'priceToBookValue', 'priceEarnings',
                        'priceToEarningsRatio', 'propertyPlantEquipmentNet', 'preferredDividendsIncomeStatementImpact',
                        'sharePriceAdjustedClose', 'priceSales', 'priceToSalesRatio', 'tradeAndNonTradeReceivables',
                        'accumulatedRetainedEarningsDeficit', 'revenues', 'revenuesUSD',
                        'researchAndDevelopmentExpense', 'returnOnAverageAssets', 'returnOnAverageEquity',
                        'returnOnInvestedCapital', 'returnOnSales', 'shareBasedCompensation',
                        'sellingGeneralAndAdministrativeExpense', 'shareFactor', 'shares', 'weightedAverageShares',
                        'weightedAverageSharesDiluted', 'salesPerShare', 'tangibleAssetValue', 'taxAssets',
                        'incomeTaxExpense', 'taxLiabilities', 'tangibleAssetsBookValuePerShare', 'workingCapital']

    def get_financials(self):
        url = "https://api.polygon.io/v2/reference/financials/{}?type=Y&sort=-reportPeriod&apiKey={}" \
            .format(self.ticker, self.api_key)

        response = requests.get(url)

        try:
            content = response.json()['results']
            df = pd.json_normalize(content).T
            df.columns = df.loc['reportPeriod']
            df.drop(['reportPeriod', 'ticker', 'period', 'updated', 'dateKey'], axis=0, inplace=True)

            return df

        except KeyError:
            return "Enter valid equity ticker."
