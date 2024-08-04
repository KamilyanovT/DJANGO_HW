from django.shortcuts import get_object_or_404, render, HttpResponse
from blog.models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F, Q

USERS_COUNT = 10
posts = Post.objects.all()

menu = [
    {"name": "Главная", "alias": "main"},
    {"name": "Блог", "alias": "blog_catalog"},
    {"name": "О проекте", "alias": "about"},
]


def about(request):
    """
    Вьюшка для страницы "О проекте"
    """
    context = {
        "users_count": USERS_COUNT,
        "menu": menu,
        "page_alias": "about",
    }

    return render(request, "about.html", context)


def blog_catalog(request):
    posts = Post.objects.all()

    if request.method == "GET":
        search = request.GET.get("search")
        search_in_title = request.GET.get("search_in_title")
        search_in_text = request.GET.get("search_in_text")
        search_in_tags = request.GET.get("search_in_tags")
        posts_filtered = []

        if search:
            query = Q()
            if search_in_title:
                query |= Q(title__icontains=search)
            if search_in_text:
                query |= Q(text__icontains=search)
            if search_in_tags:
                query |= Q(tags__name__icontains=search)
            if not search_in_title and not search_in_text and not search_in_tags:
                query |= Q(text__icontains=search)
            posts = posts.filter(query)

        context = {
            "menu": menu,
            "posts": posts,
            "page_alias": "blog_catalog",
        }
        return render(request, "blog/blog_catalog.html", context)


def index(request):
    context = {
        "users_count": USERS_COUNT,
        "menu": menu,
        "posts": posts,
        "page_alias": "main",
    }
    return render(request, "index.html", context)


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    post.views = F("views") + 1
    post.save(update_fields=["views"])
    context = {
        "menu": menu,
        "post": post,
        "page_alias": "blog_catalog",
    }
    post.refresh_from_db()
    return render(request, "blog/post_detail.html", context)


def category_detail(request, slug):
    posts = Post.objects.filter(category__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog_catalog",
    }
    return render(request, "blog/blog_catalog.html", context)


def tag_detail(request, slug):
    posts = posts = Post.objects.filter(tags__slug=slug)
    context = {
        "menu": menu,
        "posts": posts,
        "page_alias": "blog_catalog",
    }
    return render(request, "blog/blog_catalog.html", context)
