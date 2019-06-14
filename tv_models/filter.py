"""here we create search form"""
import django_filters
from .models import TVModel


class TVfilter(django_filters.FilterSet):

    class Meta:
        model = TVModel
        fields = ('screen_size', 'system_os', 'model_year', 'hdr', 'resolution')
