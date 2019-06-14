from django.urls import path
from . import views
from .views import TVDetail, TVList, FilterList
# from .views import  TVmodelCreate
urlpatterns = [
    path('', TVList.as_view(), name='tv_models-home'),
    path('about/', views.about, name='tv_models-about'),
    # path('currently_added/', views.tv_list, name="tv_models-currently_added"),
    path('model/<int:pk>/', TVDetail.as_view(), name="tv_models-tvmodel_detail"),
    path('search', FilterList.as_view(), name='tv_models-search'),
    # path('model/new/', TVmodelCreate.as_view(), name="tv_models-tvmodel_create")
]


