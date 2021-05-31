from django.urls import path
from  .views import HomeView
app_name = 'api'
urlpatterns = [
    path('home/', HomeView, name="home"),
]
