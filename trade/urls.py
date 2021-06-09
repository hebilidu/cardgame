from django.urls import path
from . import views

urlpatterns = [
    path('card/list/', views.CardListView.as_view(), name='listcard'),
    path('card/<int:pk>/view/', views.CardDetailView.as_view(), name='viewcard'),
    path('card/shuffle/', views.shuffle, name='shuffle'),
]
