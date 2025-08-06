from django import template
from ..models import Post, Comment
from django.db.models import Count
from markdown import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag()
def total_posts():
    return Post.published.count()

@register.simple_tag()
def total_comments():
    return Comment.objects.filter(active=True).count()

@register.simple_tag()
def last_post_date():
    try:
        last_post = Post.published.last()
        if last_post:
            return last_post.publish
        else:
            return None
    except AttributeError:
        return None

@register.simple_tag
def most_popular_posts(count=5):
    popular_posts = Post.published.annotate(comments_count=Count('comments')).order_by('-comments_count')[:count]
    return popular_posts

@register.inclusion_tag('partials/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}



@register.filter(name='markdown')
def to_markdown(text):
    return mark_safe(markdown(text))