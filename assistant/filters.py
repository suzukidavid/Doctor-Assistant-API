from django_filters import (
    FilterSet,
    NumberFilter,
    DateFilter,
    Filter,
)
from .models import Patient


class PatientFilter(FilterSet):
    age_min = NumberFilter(field_name='age', lookup_expr='gte')
    age_max = NumberFilter(field_name='age', lookup_expr='lte')
    star_date = DateFilter(field_name='date_of_admission', lookup_expr='gte')
    end_date = DateFilter(field_name='date_of_discharge', lookup_expr='lte')

    name = Filter(field_name='name', lookup_expr='icontains')
    phone = Filter(field_name='phone', lookup_expr='icontains')
    diagnosis = Filter(field_name='diagnosis', lookup_expr='icontains')

    class Meta:
        model = Patient
        fields = (
            'age_min',
            'age_max',
            'star_date',
            'end_date',
            'name',
            'phone',
            'diagnosis'
        )
