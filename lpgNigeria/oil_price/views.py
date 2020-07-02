from django.shortcuts import render
from django.views.generic import TemplateView
from .models import OilPrice


# Create your views here.
class OilPriceView(TemplateView):
    template_name = 'oil_price/oil_price_chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["queryset"] = OilPrice.objects.all()
        return context

