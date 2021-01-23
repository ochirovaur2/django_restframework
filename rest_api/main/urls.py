from django.urls import path
from .views import *
urlpatterns = [
    
    path('articles_api/v1/', article_list),
    path('article_api/v1/<int:pk>', artice_detail)
]
