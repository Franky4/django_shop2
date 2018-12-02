from django.db import models
from django.shortcuts import reverse


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, unique=True)
    body = models.TextField(blank=True, db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)

    def get_absolut_url(self):
        return reverse('news_detail_url', kwargs={'slug': self.slug})

    def __str__(self):
        return '{}'.format(self.title)