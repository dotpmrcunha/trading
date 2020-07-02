# Create your views here.
from rest_framework import viewsets

from app.models import Company, DailyPrice
from app.serializers import CompanySerializer, DailyPriceSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('symbol')
    serializer_class = CompanySerializer

    lookup_field = 'symbol'



class DailyPriceViewSet(viewsets.ModelViewSet):
    queryset = DailyPrice.objects.all().order_by('symbol')

    serializer_class = DailyPriceSerializer

    # http_method_names =
