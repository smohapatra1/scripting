#   https://www.geeksforgeeks.org/python/how-to-get-json-data-from-request-in-django/

import json

django-admin startproject json_project
cd json_project
django-admin startapp json_app

from django.contrib import admin
from django.urls import path
from json_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('json-handler/', views.json_handler, name='json_handler'),
]

