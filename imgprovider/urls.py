from django.contrib import admin
from django.urls import path
from django.shortcuts import redirect
from .views import *

urlpatterns = [
	path('', lambda req: redirect('/top/')),
	path('top/', display_top_of_images, name = 'top'),
    path('upload/', image_post_view, name = 'upload'), 
    #path('success/', success, name = 'success'),
]