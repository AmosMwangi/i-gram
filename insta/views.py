from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required

# , DeleteView
from .models import Post
from django.urls import reverse_lazy
from .forms import *
import users
from users.models import Profile


class HomePageView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "insta/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]


class PostDetailView(DetailView):
    model = Post
    template_name = "insta/detail.html"


# class CreatePostView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = "insta/post.html"
#     success_url = reverse_lazy("home")

@login_required(login_url="/accounts/login/")
def create_post(request):
  '''
  view function that renders a form for creating a new post
  '''  
  if request.method=='POST':
    form=PostForm(request.POST,request.FILES)
    if form.is_valid():
      post=form.save(commit=False)
      post.author=request.user
      post.save()

      return redirect('home')
  else:
    form=PostForm()    
    
  return render(request,'insta/post.html',{"form":form})  


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "insta/update.html"
    success_url = reverse_lazy("home")


# class PostDeleteView(DeleteView):
#    model = Post
#    template_name = 'insta/confirm_delete.html'

#    def get_success_url(self):
#       return reverse_lazy('home')

#    @method_decorator(login_required)
#    def dispatch(self, request, *args, **kwargs):
#       return super(PostDeleteView, self).dispatch(request, *args, **kwargs)


def comment(request, id):
    if request.method == "POST":
        image = get_object_or_404(Images, id=id)
        form = CommentForm(request.POST)

        if form.is_valid():
            imageComment = form.save(commit=False)
            imageComment.posted_by = request.user
            images = Images.objects.get(id=id)
            imageComment.image_id = images
            imageComment.save()
            return redirect("home")

    else:
        form = CommentForm()
        image = get_object_or_404(Post, id=id)
        id = image.id
    return render(request, "insta/home.html", {"form": form, "id": id})


def comment_view(request, id):
    image = Post.objects.filter(id=id)
    comments = Comment.objects.filter(post_id=id)
    return render(request, "insta/home.html", {"image": image, "comments": comments})


def like(request):
    user = request.user
    image = get_object_or_404(Post, id=request.POST.get("post.id"))
    if image.liked.filter(id=user.id).exists():
        image.liked.remove(user)
    else:
        image.liked.add(request.user)
    return redirect("home")


def follow(request):
    user = request.user
    follow = get_object_or_404(Profile, user=request.POST.get("usr.id"))
    if follow.followers.filter(id=user.id).exists():
        follow.followers.remove(user)
    else:
        follow.followers.add(user)
    return redirect("home")

