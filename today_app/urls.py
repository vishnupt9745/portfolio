from django.urls import path

import my

from today_app import views

urlpatterns = [
   path('first_template',views.first_template,name='first_template'),
   path('second_template',views.second_template,name='second_template'),
   path('index',views.index,name='index')
]