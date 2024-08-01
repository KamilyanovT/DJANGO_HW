import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()



@register.simple_tag(name='markdown_to_html')
def markdown_to_html(markdown_text: str) -> str:

    md_extensions = ['extra', 'fenced_code', 'tables']
    html_content = markdown.markdown(markdown_text, extensions=md_extensions)

    return mark_safe(html_content)