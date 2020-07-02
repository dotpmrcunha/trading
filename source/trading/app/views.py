# Create your views here.
from rest_framework import viewsets, generics
from django_filters import rest_framework as filters

from app.filters import DailyPriceFilter
from app.models import Company, DailyPrice
from app.serializers import CompanySerializer, DailyPriceSerializer


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
