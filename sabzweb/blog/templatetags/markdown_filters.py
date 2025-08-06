# blog/templatetags/markdown_filters.py
import markdown
from django import template

register = template.Library()

@register.filter
def markdownify(text):
    if text:
        return markdown.markdown(text)
    return ""
