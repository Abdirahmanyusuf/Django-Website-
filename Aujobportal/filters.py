import django_filters
from . models import *


class jobRegisterFilter(django_filters.FilterSet):
    class Meta:
        Model = jobRegister
        fields = ('position', 'Location', 'Department')
