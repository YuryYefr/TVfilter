from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TVModel
from django.views.generic import DetailView as DV, ListView as LV
from .filter import TVfilter


def about(request):
    return render(request, 'tv_models/about.html')


class TVList(LV):
    """List of models with pagination"""
    model = TVModel
    template_name = 'tv_models/home.html'
    context_object_name = 'model'
    paginate_by = 5


class FilterList(LV):
    """search logic"""
    model = TVModel
    template_name = 'tv_models/search.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['filter'] = TVfilter(self.request.GET, queryset=self.get_queryset())
        return ctx


class TVDetail(DV):
    """detailed view of every model"""
    model = TVModel


