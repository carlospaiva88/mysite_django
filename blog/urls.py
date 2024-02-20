from django.urls import path

from blog import views
from .views.post_view import PostView

urlpatterns = [
    path('', views.Postview.as_views(), name='home')
]