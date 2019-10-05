from django.urls import path
from .View.principal import index
urlpatterns = [

path('', index, name='home'),

]