from django.db import models


class Company(models.Model):

    company_id = models.UUIDField(primary_key=True, unique=True)

    FINANCIALS, UTILITIES, CONSUMER, STAPLES, ENERGY, HEALTH_CARE, INDUSTRIALS, TECHNOLOGY, TELECOM, MATERIALS, REIT = (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    )

    SECTOR_TYPES = (
        (FINANCIALS, "Financials"),
        (UTILITIES, "Utilities"),
        (CONSUMER, "Consumer Discretionary"),
        (STAPLES, "Consumer Staples"),
        (ENERGY, "Energy"),
        (HEALTH_CARE, "Health Care"),
        (INDUSTRIALS, "Industrials"),
        (TECHNOLOGY, "Technology"),
        (TELECOM, "Telecommunications"),
        (MATERIALS, "Matirials"),
        (REIT, "REIT"),
    )
    sector = models.IntegerField(choices=SECTOR_TYPES)

    address = models.CharField(max_length=200)
    symbol = models.CharField(max_length=10, unique=True)
    short_name = models.CharField(max_length=28)


class DailyPrice(models.Model):

    symbol = models.CharField(max_length=10)

    open = models.DecimalField(max_digits=15, decimal_places=4)
    high = models.DecimalField(max_digits=15, decimal_places=4)
    low = models.DecimalField(max_digits=15, decimal_places=4)
    close = models.DecimalField(max_digits=15, decimal_places=4)

    volume = models.PositiveIntegerField()

    date = models.DateField(unique_for_date=True)

    class Meta:
        unique_together = [['symbol', 'date']]
        indexes = [
            models.Index(fields=['symbol', 'date']),
        ]
