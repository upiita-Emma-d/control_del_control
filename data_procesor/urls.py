from django.urls import path
from data_procesor import views
urlpatterns = [
    path('', views.procesadorView.as_view()),
]
