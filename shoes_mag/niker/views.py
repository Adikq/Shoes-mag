from django.db.models import Q
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .forms import OrderForm
from .models import Shoes


# menu = [
#     {'title': 'Отзывы', 'url_name': 'home'}
# ]



class ShoesView(ListView):
    model = Shoes
    template_name = 'niker/index.html'
    
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['menu'] = menu
    #     return context


class ShoesDetail(DetailView):
    model = Shoes
    template_name = 'niker/shoes_detail.html'
    slug_field = 'slug'


class CategoryView(ListView):
    model = Shoes
    template_name = 'niker/category_filter_views.html'

    def get_queryset(self):
        return Shoes.objects.filter(category__slug=self.kwargs['slug'])

class Search(ListView):

    template_name = 'niker/category_filter_views.html'

    def get_queryset(self):
        return Shoes.objects.filter(title__icontains=self.request.GET.get('q'))


class AddOrder(View):
    def post(self, request, pk):
        form = OrderForm(request.POST)
        shoes = Shoes.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.shoes = shoes
            form.save()
        return redirect(shoes.get_absolute_url())


class FilterShoes(ListView):
    template_name = 'niker/category_views.html'

    def get_queryset(self):
        queryset = Shoes.objects.filter(
            Q(color=self.request.GET.getlist('color'))
        )
        return queryset


