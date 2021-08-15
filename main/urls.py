from django.urls import path
from .views import homepage, about, calc

urlpatterns = [
    path('', homepage),
    path('about/<str:name>', about),
    path('calc/<int:num>', calc)
]