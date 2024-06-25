from django.http import HttpResponse, Http404
from django.shortcuts import render

CATEGORIES = {
    1: "Чилл территории Python",
    2: "Django, сложно, но можно!",
    3: "Flask, бегите, глупцы!",
}


def blog_catalog(request):
    return HttpResponse(
        """<h1>Тут будет блог</h1>
                           <a href="/category/">Категории</a>"""
    )


def category_list(request):
    categories = ", ".join([str(key) for key in CATEGORIES.keys()])
    return HttpResponse("<ul><li>Python</li><li>Django</li><li>Flask</li></ul>")


def category_detail(request, category_id):
    category_id = int(category_id)
    category_str = CATEGORIES.get(category_id)
    context = {"massage": category_str}
    if not category_str:
        raise Http404(f"Категория с id={category_id} не найдена")
    return render(request, "python_blog/test_template.html", context=context)
