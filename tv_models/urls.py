from django.urls import path
from . import views
from .views import TVDetail, TVList, FilterList
urlpatterns = [
    path('', TVList.as_view(), name='tv_models-home'),
    path('about/', views.about, name='tv_models-about'),
    path('model/<int:pk>/', TVDetail.as_view(), name="tv_models-tvmodel_detail"),
    path('search', FilterList.as_view(), name='tv_models-search'),
]


