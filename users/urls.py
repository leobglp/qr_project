from django.urls import path
from . import views
from .views import (
    CardCreateView,
    CardUpdateView,
    CardDeleteView
)

urlpatterns = [
    path('', views.about, name='about-page'),
    path('card/new/', CardCreateView.as_view(), name='card-create'),
    path('card/<int:pk>/update/', CardUpdateView.as_view(), name='card-update'),
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='card-delete'),
]
