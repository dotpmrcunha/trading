from __future__ import absolute_import, unicode_literals

from celery import shared_task
from datetime import datetime as dt

from app.models import Company, DailyPrice
import yfinance as yf


@shared_task
def add_daily_information():
    for c in Company.objects.all().values("company_id", "symbol"):
        history = yf.Ticker(c.get('symbol')).history(period="1d", interval="1d")

        for date in history.index:
            if not DailyPrice.objects.filter(symbol=c.get('symbol'), date=dt(date.year, date.month, date.day)).exists():
                DailyPrice.objects.create(
                    company_id=c.get("company_id"),
                    symbol=c.get('symbol'),
                    open=float(history.at[date, "Open"][0]),
                    high=float(history.at[date, "High"][0]),
                    low=float(history.at[date, "Low"][0]),
                    close=float(history.at[date, "Close"][0]),
                    volume=float(history.at[date, "Volume"][0]),
                    date=dt(date.year, date.month, date.day)
                )
