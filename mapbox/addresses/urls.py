from django.urls import path
from .views import AddressView, some_func

urlpatterns = [
   path('', AddressView.as_view(), name='home'),
   path('random_url/', some_func)
]