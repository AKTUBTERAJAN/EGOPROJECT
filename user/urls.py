from django.urls import path
from . import views
urlpatterns=[
    path('index/', views.index),
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('volunteer/', views.ourvolunteers),
    path('vission mission/', views.vissionmission),
    path('upcomingevent/',views.event),
    path('viewevent/',views.event),
    path('donatenow/',views.donatenow),
    path('help/',views.help),
    path('stories & change/',views.story),
    path('volunteerlist/',views.volunteerslist),
]
