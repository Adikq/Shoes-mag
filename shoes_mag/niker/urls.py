from django.urls import path

from .views import ShoesView, FilterShoes, ShoesDetail, AddOrder, CategoryView, Search

urlpatterns = [
    path('', ShoesView.as_view(), name='home'),
    path('shoes/<slug:slug>', ShoesDetail.as_view(), name='shoes_detail'),
    path('category/<slug:slug>', CategoryView.as_view(), name = 'category'),
    path('filter-shoes', FilterShoes.as_view(), name='filter'),
    path('addorder/<int:pk>', AddOrder.as_view(), name='addorder'),
    path('shoes/', Search.as_view(), name='search')
]

