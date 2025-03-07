# blog/models.py
from django.db import models
from django.urls import reverse # Новый импорт
 
 
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    def __str__(self):
        return self.title
 
    def get_absolute_url(self): # Тут мы создали новый метод
        return reverse('post_detail', args=[str(self.id)])