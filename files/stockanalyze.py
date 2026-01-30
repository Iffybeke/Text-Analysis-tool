import yfinance as yf
def extractBasicStockInfo(data):
    keysToExtract = ['longName', 'website', 'sector', 'industry', 'fullTimeEmployees', 'city', 'state', 'country', 'zip', 'phone', 'marketCap', 'beta', 'forwardPE', 'dividendYield']
    basicInfo = {}
    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key]
   else:
            basicInfo[key] = ""
   
    return basicInfo
def getCompanyStockInfo(ticker_symbol):
    company = yf.Ticker(ticker_symbol)
    basicInfo = extractBasicStockInfo(company.info)
    print(basicInfo)

    getCompanyStockInfo("MSFT")