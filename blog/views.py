from django.shortcuts import get_object_or_404, render, HttpResponse
from blog.models import Post
from django.shortcuts import get_object_or_404

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
    if request.method == "GET":
        search = request.GET.get("search")
        search_in_title = request.GET.get("searchInTitle")
        search_in_text = request.GET.get("searchInText")
        search_in_tags = request.GET.get("searchInTags")
        posts_filtered = []

        if search:

            for post in posts:
                if not search_in_title and not search_in_text and not search_in_tags:
                    if search.lower() in post["text"].lower():
                        posts_filtered.append(post)
                if search_in_title:
                    if search.lower() in post["title"].lower():
                        posts_filtered.append(post)
                if search_in_text:
                    if search.lower() in post["text"].lower():
                        posts_filtered.append(post)
                if search_in_tags:
                    for tag in post["tags"]:
                        if search.lower() in tag.lower():
                            posts_filtered.append(post)

        context = {
            "menu": menu,
            "posts": posts_filtered if posts_filtered else posts,
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
    post = get_object_or_404(Post, slug=slug)
    context = {        "menu": menu,
        "post": post,
        "page_alias": "blog_catalog",
    }
    return render(request, "blog/post_detail.html", context)
