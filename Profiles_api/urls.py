from django.urls import path
from Profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
]
