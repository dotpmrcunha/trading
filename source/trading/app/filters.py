from django_filters import rest_framework as filters

from app.models import DailyPrice


class DailyPriceFilter(filters.FilterSet):

    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = DailyPrice
        fields = ['start_date', 'end_date']
