
from django.shortcuts import render
from django.urls import path
from .import views
urlpatterns=[
    path('', views.form_view, name='form'),
    path('submit/', views.submit_form, name='submit_form'),
    path('family/<str:family_id>', views.family_page, name='family_page')
]
    