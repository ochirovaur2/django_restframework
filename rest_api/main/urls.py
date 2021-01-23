from django.urls import path
from .views import *
urlpatterns = [
    
    path('articles_api/v1/', article_list),
    path('article_api/v1/<int:pk>', artice_detail),
    path('list_of_users_api/v1/', ListUsers.as_view()),
  	path('articles_api/v2/', Article_list.as_view()),
  	path('article_api/v2/<int:pk>', Artice_detail.as_view()),
  	
]
