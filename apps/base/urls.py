from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('contact/', views.contact_view, name='contact'),  # Маршрут для формы контактов
]

