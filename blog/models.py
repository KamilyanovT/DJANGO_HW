from random import choices
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
    category = models.ForeignKey(
        "Category",
        on_delete=models.CASCADE,
        related_name="posts",
        null=True,
        default=None,
    )
    tags = models.ManyToManyField("Tag", related_name="posts")
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == "":
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if self.slug == None or self.slug == "":
            self.slug = slugify(unidecode(self.name))
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return self.name

    def get_absolute_url(self):
        return f"/blog/category/{self.slug}/"


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))
        self.name = self.name.lower().replace(" ", "_")
        super().save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return self.name

    def get_absolute_url(self):
        return f"/blog/tag/{self.slug}/"


class Comment(models.Model):
    STATUS_CHOICES = [
        ("checked", "Проверен"),
        ("unchecked", "Не проверен"),
    ]
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="unchecked"
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self, *args, **kwargs):
        return self.text
