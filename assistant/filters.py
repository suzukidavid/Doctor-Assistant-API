from django_filters import (
    FilterSet,
    NumberFilter,
    DateFilter,
)
from .models import Patient


class PatientFilter(FilterSet):
    age_min = NumberFilter(field_name='age', lookup_expr='gte')
    age_max = NumberFilter(field_name='age', lookup_expr='lte')
    star_date = DateFilter(field_name='date_of_admission', lookup_expr='gte')
    end_date = DateFilter(field_name='date_of_discharge', lookup_expr='lte')

    # name = Filter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Patient
        fields = '__all__'
        # fields = ('age_min', 'age_max', 'star_date', 'end_date')