from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address

# Create your views here.
class AddressView(CreateView):

   model = Address
   fields = ['address']

   template_name = 'addresses/home.html'
   success_url = '/'

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['mapbox_access_token'] = 'pk.eyJ1Ijoia2dhdHRpIiwiYSI6ImNsOTNjbmU2ZzF0NzYzbm1mdXBzcWl2eXgifQ.5e8SPJh6Q7-eCfX3vI42EA'
      context['addresses'] = Address.objects.all()
      return context