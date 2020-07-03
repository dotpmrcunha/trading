import json
from datetime import datetime as dt

import numpy
import yfinance as yf
from django.http import HttpResponse
from django_filters import rest_framework as filters
from rest_framework import viewsets, generics

from app.filters import DailyPriceFilter
from app.models import Company, DailyPrice
from app.serializers import CompanySerializer, DailyPriceSerializer, RecommendationSerializer

SCALAR_VECTOR = {
    "Buy": 1,
    "Neutral": 0,
    "String Buy": 1.5,
    "Sell": -1,
    "Strong Sell": -1.5,
    "Positive": 1,
    "Negative": -1
}


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('symbol')
    serializer_class = CompanySerializer

    lookup_field = 'symbol'


class DailyPriceViewSet(generics.ListAPIView):
    serializer_class = DailyPriceSerializer

    filter_backends = (filters.DjangoFilterBackend,)

    filterset_class = DailyPriceFilter

    def get_queryset(self):
        return DailyPrice.objects.filter(symbol=self.kwargs['symbol'])


class RecommendationViewSet(generics.ListAPIView):

    serializer_class = RecommendationSerializer

    @staticmethod
    def transform_results(results):
        final_result = dict()
        for r in results:
            date = f"{str(r.get('date').day).zfill(2)}-{str(r.get('date').month).zfill(2)}-{r.get('date').year}"
            if date not in final_result:
                final_result[date] = [r.get("grade")]
            else:
                final_result[date].append(r.get("grade"))
        return [{'date': k, 'recommendation': numpy.mean(final_result.get(k))} for k in final_result]

    def get_queryset(self):
        rec = yf.Ticker(self.kwargs['symbol']).recommendations
        start_date = dt.strptime(self.request.GET.get("start_date"), '%d-%m-%Y')
        end_date = dt.strptime(self.request.GET.get("end_date"), '%d-%m-%Y')
        timestamps = list(filter(lambda x: start_date < x < end_date, rec.index))
        return self.transform_results(
            [{"date": t, "grade": SCALAR_VECTOR.get(rec.at[t, 'To Grade'], 0)} for t in timestamps]
        )

    def validate_request(self):
        error_message = {}
        for k in ['start_date', 'end_date']:
            if k not in self.request.GET:
                error_message[k] = f"'{k}' not in the URL as query parameters"
            else:
                try:
                    dt.strptime(self.request.GET.get(k), '%d-%m-%Y')
                except ValueError:
                    error_message[k] = f"'{k}' is not a valid date format (DD-MM-YYYY)"
        return error_message

    def get(self, request, *args, **kwargs):
        error_message = self.validate_request()
        if error_message:
            return HttpResponse(content=json.dumps(error_message), status=400, content_type='application/json')
        return super().get(request, *args, **kwargs)


