from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('form/',form),
    path('show_data/',show_data),
    path('form/data.html/',show_data),
]
