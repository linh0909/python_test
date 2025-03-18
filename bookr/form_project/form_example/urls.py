from django.contrib import admin
from django.urls import path
from .views import form_example

urlpatterns = [
    path('form-example/', form_example, name='form_example')
]