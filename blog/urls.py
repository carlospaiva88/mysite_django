from django.urls import path

from blog import views
from .views.post_view import PostView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

]