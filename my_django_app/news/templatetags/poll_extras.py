from unicodedata import name
from django import template
from news.models import * 
register=template.Library()

@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Post.objects.all()
    else:
        return Post.objects.filter(pk=filter)

@register.inclusion_tag('news/list_categories.html')
def show_categories(sort=None,cat_selected=0):
    if not sort:
        cats=Post.objects.all()
    else:
        cats=Post.objects.order_by(sort)
    return {'cats':cats,'cat_selected':cat_selected}