from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address
from django.http import HttpResponse
import json

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

def some_func(request):
    if request.method == 'GET':
        param1 = request.GET.get('param_first')
        param2 = request.GET.get('param_second')

        response_data = 'success!'

        return HttpResponse(
            json.dumps({"latitude": param1, "longitude": param2}),
            content_type="appliction/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "yeet"}),
            content_type="application/json"
        )
