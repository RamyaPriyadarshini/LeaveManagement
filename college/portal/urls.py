from django.urls import path
from . import views

urlpatterns = [
    path('', views.portal, name='portal-home'),
    path('profile/', views.profile, name='portal-profile'),
]
