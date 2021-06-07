from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/list/', views.PostListView.as_view(), name='listpost'),
    path('post/add/', views.PostAddView.as_view(), name='addpost'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'viewpost'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='editpost'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='deletepost')
]
