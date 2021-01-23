from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 
from .serializers import ArticleSerializer
from .models import Article
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

@api_view(['GET', 'POST'])
def article_list(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		print(serializer.data)
		
		return Response( serializer.data , status=status.HTTP_201_CREATED)

	elif request.method == 'POST':
		
		serializer = ArticleSerializer(data=request.data)
		print(serializer) 
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artice_detail(request, pk):
	
	try:
		article = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		return  Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':

		serializer = ArticleSerializer(article)
		print(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	elif request.method == 'PUT':
		
		serializer = ArticleSerializer(article, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		article.delete()
		return Response({'status': 'success'} ,status=status.HTTP_204_NO_CONTENT)


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User

class ListUsers(APIView):
    """
    View to list all users in the system.

    
    * Only admin users are able to access this view.
    """
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class Article_list(APIView):
	"""docstring for Article_list"""
	def get(self, request):
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)
		print(serializer.data)
		
		return Response( serializer.data , status=status.HTTP_201_CREATED)

	def post(self, request):
		print(request.data)
		serializer = ArticleSerializer(data=request.data)
		
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Artice_detail(APIView):
	"""docstring for Article"""
	
	def get_objects(self, pk):

		try:
			article = Article.objects.get(id=pk)
			return article
		except Article.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

	def get(self, request, pk):
		article = self.get_objects(pk)
		print(article)
		serializer = ArticleSerializer(article)
		print(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED)