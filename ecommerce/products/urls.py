from django.urls import path
from .views import Home

# urlpatterns
app_name = 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('cart/<slug>', add_to_cart, name='cart')
    path('remove/<slug>', remove_from_cart, name='cart')

]
