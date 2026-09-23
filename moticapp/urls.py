from django.urls import path
from moticapp import views

urlpatterns = [
    path('', views.index, name='index'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    path('teams/', views.teams, name='teams'),
    path('battle/', views.battle, name='battle'),
    path('gallery/', views.gallery, name='gallery'),
    path('tickets/', views.tickets, name='tickets'),
]