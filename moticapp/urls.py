
from django.contrib import admin
from django.urls import path


from moticapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('starter/', views.starter, name='starter'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),



    path(
        'team/register/',
        views.team_registration,
        name='team_registration'
    ),

     path(
       'team/success/<int:team_id>/',
        views.team_success,
         name='team_success'
      ),

     path(
      'team/ticket/<int:team_id>/',
      views.team_ticket,
      name='team_ticket'
     ),
      path('teams/', views.teams, name='teams'),
       path('battle/', views.battle, name='battle'),
      path('gallery/', views.gallery, name='gallery'),
      path('tickets/', views.tickets, name='tickets'),
      path('tickets/', views.tickets, name='tickets'),

    path(
       'tickets/book/',
      views.ticket_booking,
      name='ticket_booking'
     ),

      path(
        'tickets/success/<int:booking_id>/',
          views.ticket_success,
          name='ticket_success'
      ),
     path(
      'tickets/qr/<int:booking_id>/',
      views.ticket_qr,
      name='ticket_qr'
      ),







]

