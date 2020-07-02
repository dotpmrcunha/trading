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

    def get_company_data(self, symbol: str, days: int = 31):
        res = yf.Ticker(symbol).history()
        date = dt.now() - relativedelta(months=1)

        for i in range(days):
            string_date = dt.strftime(date + relativedelta(days=i), "%Y-%m-%d")
            if res.get("High").get(string_date) is not None:
                element = {
                    "model": "app.dailyprice",
                    "pk": self.id,
                    "fields": {
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
        with open(f'price.json', 'w') as outfile:
            json.dump(self.result, outfile)


get_price = GetPrice()

for ticket in ["MSFT", "AAPL"]:
    get_price.get_company_data("MSFT")

get_price.save_json()