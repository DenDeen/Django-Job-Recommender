from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # The data
    path('data/', views.data, name='data'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
