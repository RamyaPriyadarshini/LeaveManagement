from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'portal'
urlpatterns = [
    path('', views.login, name='login'),
    path('index/', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    path('add/', views.PersonalCreate.as_view(), name='personal-add'),
    path('register/', views.UserFormView.as_view(), name='register')
]
