from django.urls import path
from . import views

app_name = 'sponsors'

urlpatterns = [
    path('', views.sponsors, name='sponsors'),
    path('support_us/', views.support_us,name='support_us'),
    path('prospectus/', views.sponsors, name='Prospectus'),
]
