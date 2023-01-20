# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 21:25:23 2023

@author: 86177
"""

from django.urls import path
from rango import views 

app_name = 'rango'

urlpatterns = [
    path('', views.index, name = 'index'),
    
    ]