import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(name="markdown_to_html")
def markdown_to_html(markdown_text: str) -> str:

    html = markdown.markdown(markdown_text)
    return mark_safe(html)
