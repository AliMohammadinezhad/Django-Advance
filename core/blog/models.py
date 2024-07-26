from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Profile

# getting the current user model
User = get_user_model()

class Post(models.Model):
    """
    This is a class representing a post model for the blog app.
    """
    author = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()
    
    
    def __str__(self) -> str:
        return self.title
    
    def get_absolute_api_url(self):
        return reverse("blog:api-v1:post-detail", kwargs={"pk": self.pk})
    
    def get_brief_content(self):
        return self.content[0:5]
    
    
    
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name    
    