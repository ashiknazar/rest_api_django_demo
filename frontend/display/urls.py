from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Homepage view to render HTML
]
