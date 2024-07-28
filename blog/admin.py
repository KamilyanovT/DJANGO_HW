from django.contrib import admin
from .models import Post, Category, Tag, Comment

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_date", "updated_date")
    search_fields = ("title", "text")
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)

admin.site.register(Tag)

admin.site.register(Comment)