from django.urls import path # type: ignore
from .views import dashboard


urlpatterns = [
path('', dashboard, name='dashboard'),
]