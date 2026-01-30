import yfinance as yf
from datetime import datetime
def extractBasicStockInfo(data):
    keysToExtract = ['longName', 'website', 'sector', 'industry', 'fullTimeEmployees', 'city', 'state', 'country', 'zip', 'phone', 'marketCap', 'beta', 'forwardPE', 'dividendYield']
    basicInfo = {}
    for key in keysToExtract:
        if key in data:
            basicInfo[key] = data[key]
    else:
            basicInfo[key] = ''
   
    return basicInfo

def getPriceHistory(company):
    historyDf = company.history(period='12mo')
    prices = historyDf['Open'].tolist()
    dates= historyDf.index.strftime('%Y-%m-%d').tolist()
    return{
        'dates': dates,
        'prices': prices
    }
    

def getEarningsDates(company):
    earningDatesDf = company.earnings_dates
    allDates = earningDatesDf.index.strftime('%Y-%m-%d').tolist()
    dateObjects = {datetime.strptime(date, '%Y-%m-%d') for date in allDates}
    currentDate = datetime.now()
    futureEarningsDates = [date.strftime('%Y-%m-%d') for date in dateObjects if date > currentDate]
    return futureEarningsDates

    def getCompanyNews(company):
        newsList = company.news
        allNewsArticles = []
        for newsDict in newsList:
            newsDictToAdd = {
                'title': newsDict.get('title', ''),
                'link': newsDict.get('link', ''),
                'publisher': newsDict.get('publisher', ''),
                'providerPublishTime': datetime.fromtimestamp(newsDict.get("providerPublishTime", 0)).strftime('%Y-%m-%d %H:%M:%S')
            }
            allNewsArticles.append(newsDictToAdd)
        print(allNewsArticles)
        return allNewsArticles

        def extractCompanyNewsArticles(newsArticles):
            print(newsArticles)

        def getCompanyStockInfo(tickerSymbol):
            #Get data from yahoo finance
            company = yf.Ticker(tickerSymbol)

            #get basic stock info
            basicInfo = extractBasicStockInfo(company.info)
            priceHistory = getPriceHistory(company)
            futureEarningsDates = getEarningsDates(company)
            newsArticles = getCompanyNews(company)


    getCompanyStockInfo('MSFT')