from django.urls import path
from . import views

urlpatterns = [
    path('', views.showblogs,  name='showblogs'),
    path('<int:blog_id>/', views.detail,  name='blog-detail'),
]