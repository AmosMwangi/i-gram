from django.urls import path

from .views import HomePageView, PostDetailView, CreatePostView, UpdatePostView

# , DeletePostView
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/", CreatePostView.as_view(), name="add_post"),
    path("post/<int:pk>/update/", UpdatePostView.as_view(), name="update_post"),
    # path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),

    
]

