from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    cat_title = models.CharField(max_length=255, verbose_name='Категория')  
    slug = models.SlugField(max_length=200, null=True, unique=True)

    def __str__(self):
        return self.cat_title

    def save(self,  *args, **kwargs):
        self.slug = slugify(self.cat_title)
        return super(Category, self).save(*args, **kwargs)
    
    class Meta():
        verbose_name='Категория'
        verbose_name_plural='Категории'

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  
    slug = models.SlugField(max_length=200, null=True, unique=True) 
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')])  
    content = models.TextField()
    updated = models.DateTimeField(default=timezone.now)  
    publication_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self,  *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)
    
    class Meta():
        verbose_name='Пост'
        verbose_name_plural='Посты'