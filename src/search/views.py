from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product

class SearchProductView(ListView):
    # queryset = Product.objects.all()
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        context["query"] = self.request.GET.get('q')
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = request.GET.get('q', None) # method_dict['q']
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.features()
