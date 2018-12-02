from django.urls import path

from .views import *

urlpatterns = [
    path('', info_view, name='news_list_url'),
    path('info/<str:slug>/', news_detail, name='news_detail_url'),

]

