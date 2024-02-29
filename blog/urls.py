from django.urls import path
from .views.post_view import PostDetail, PostView

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail')
]