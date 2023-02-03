# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 06:36:37 2023

@author: 86177
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                     'tango_with_django_project.settings')

import django 
django.setup()

from rango.models import Category, Page

def populate():
    
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 114},
        {'title': 'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython',
         'views': 11},
        {'title':'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 150}]
    
    django_pages = [{'title': 'Official Django Tutorial',
         'url': 'http://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 1},
        {'title': 'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 1145},
        {'title':'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 11451}]
    
    other_pages = [
        {'title': 'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 12},
        {'title':'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 198}]
    
    python_category = {'name': 'Python',
                       'views': 128,
                       'likes': 64}
    
    django_category = {'name': 'Django',
                       'views': 64,
                       'likes': 32}
    
    other_frameworks_category = {'name': 'Other Frameworks',
                       'views': 32,
                       'likes': 16}
    
    cats = {python_category['name']:{'pages': python_pages, 'categorys':python_category },
            django_category['name']:{'pages': django_pages, 'categorys':django_category },
            other_frameworks_category['name']:{'pages': other_pages, 'categorys': other_frameworks_category}}
     
    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data['categorys']['views'], cat_data['categorys']['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])
            
    for c in Category.objects.all():
        print(f"{c.name}'s views: {c.views}")
        print(f"{c.name}'s likes: {c.likes}")
        for p in Page.objects.filter(category = c):
            print(f'{c}: {p}')
            print(f'the total views of {p.title}: {p.views}')
           
            
def add_page(cat, title, url, views = 0):
    p = Page.objects.get_or_create(category = cat, title = title)[0]
    p.url = url 
    p.views = views
    p.save()
    return p 
    
def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name = name)[0]
    c.views = views 
    c.likes = likes 
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
    