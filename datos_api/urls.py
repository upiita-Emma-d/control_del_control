from django.urls import path 
from datos_api import views
urlpatterns = [
    path('adc/', views.Modelado.as_view()),
]