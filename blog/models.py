from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from unidecode import unidecode


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    data = models.JSONField()
    published_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == "":
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return f"{self.title}: {self.slug}"

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"
