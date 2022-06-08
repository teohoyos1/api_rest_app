from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from api import views


urlpatterns = [
    path('', views.api_home, name="get_api"),
    path('add/', views.api_post_home, name="post_api"),
    path('auth/', obtain_auth_token)
]