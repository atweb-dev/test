from django.urls import path
from . import views

urlpatterns = [
    path('', views.mes, name='mes'),
    path('logout/', views.lgt, name='lgt'),
]
