from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import TVModel
from django.views.generic import DetailView as DV, ListView as LV, CreateView as CW
from .filter import TVfilter


# Create your views here.
# just reserve
# def home(request):
#     ctx = {}
#     ctx['model'] = TVModel.objects.all()
#     return render(request, 'tv_models/home.html', ctx)


def about(request):
    return render(request, 'tv_models/about.html')


# def tv_list(request):
#     content = {}
#     content['model'] = TVModel.objects.all()
#     content['current_tab'] = 'main'
#     return render(request, 'tv_models/currently_added.html', content)


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

# def search(request):
#     ctx = {}
#     if request.method == 'GET':
#         try:
#             q = request.GET.get('query')
#             ctx['model'] = TVModel.objects.filter(screen_size=q)
#             ctx['select'] = TVModel.S_SIZE
#             ctx['q'] = [elem[1] for elem in TVModel.S_SIZE if elem[0] == q][0]
#         except Exception as e:
#             ctx['model'] = TVModel.objects.all()
#         return render(request, 'tv_models/home.html', ctx)

# maybe in future
# class TVmodelCreate(LoginRequiredMixin, CW):
#     model = TVModel
#     fields = ['title', 'model_year', 'screen_size', 'resolution', 'hdr', 'system_os', 'content']
#
#     def create_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
