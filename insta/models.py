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



    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    



