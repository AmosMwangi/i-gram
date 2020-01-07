from django.urls import path

from .views import HomePageView, PostDetailView, UpdatePostView

# , DeletePostView
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    # path("post/", CreatePostView.as_view(), name="add_post"),
    path('create_post',views.create_post,name="create_post"),
    path("post/<int:pk>/update/", UpdatePostView.as_view(), name="update_post"),
    # path('post/<int:pk>/delete/', DeletePostView.as_view(), name='delete_post'),
    
    path("like/", views.like, name="like"),
    path("follow/", views.follow, name="follow"),
    path("comment/view/<int:id>/",views.comment_view, name = "view"),
    path("comment/new/<int:id>/", views.comment, name="comment"),
    
]

