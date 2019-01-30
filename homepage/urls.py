from django.urls import path

from . import views

# namespace
app_name = 'homepage'

urlpatterns = [
    path('',  views.index, name='index'),
]
