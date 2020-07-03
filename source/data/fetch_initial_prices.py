import json
from datetime import datetime as dt

import yfinance as yf
from dateutil.relativedelta import relativedelta


class GetPrice:

    __id = 0
    __result = []

    def __init__(self, days=31):
        self.days = days

    @property
    def id(self):
        self.__id += 1
        return self.__id

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, value):
        self.__result.append(value)

    def get_company_data(self, symbol: str, company_id: str, days: int = 31):
        res = yf.Ticker(symbol).history()
        date = dt.now() - relativedelta(months=1)

        for i in range(days):
            string_date = dt.strftime(date + relativedelta(days=i), "%Y-%m-%d")
            if res.get("High").get(string_date) is not None:
                element = {
                    "model": "app.dailyprice",
                    "pk": self.id,
                    "fields": {
                        "company_id": company_id,
                        "symbol": symbol,
                        "open": float(res.get("Open").get(string_date)),
                        "high": float(res.get("High").get(string_date)),
                        "low": float(res.get("Low").get(string_date)),
                        "close": float(res.get("Close").get(string_date)),
                        "volume": int(res.get("Volume").get(string_date)),
                        "date": string_date
                    }
                }
                self.result = element

    def save_json(self):
        with open(f'source/data/price.json', 'w') as outfile:
            json.dump(self.result, outfile)


def get_companies():
    companies = []
    with open(f'source/data/company.json', 'r') as infile:
        info = json.load(infile)
        for i in info:
            companies.append((i.get('fields').get('symbol'), i.get('pk')))
    return companies


get_price = GetPrice()
for ticket, company_id in get_companies():
    get_price.get_company_data(ticket, company_id)

get_price.save_json()