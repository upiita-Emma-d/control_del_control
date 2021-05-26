from django.urls import path
from profiles_api import views


urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('datos/',views.DATOS.as_view()),
]
