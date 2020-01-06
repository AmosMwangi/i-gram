from django.db import models
from django.utils import timezone
from django.urls import reverse
from PIL import Image
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='images/')
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    liked = models.ManyToManyField(User,blank= True,related_name='post_likes')
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    

class Comment(models.Model):
    comment = HTMLField()
    posted_by = models.ForeignKey(User, on_delete = models.CASCADE)
    posted_on = models.DateField(auto_now_add=True)
    post_id = models.ForeignKey(Post,on_delete= models.CASCADE)



