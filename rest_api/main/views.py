from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser 
from .serializers import ArticleSerializer
from .models import Article
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def article_list(request):
	if request.method == 'GET':
		articles = Article.objects.all()
		serializer = ArticleSerializer(articles, many=True)

		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(data=data)

		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, 500)


@csrf_exempt
def artice_detail(request, pk):
	print(pk)
	try:
		article = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
		return JsonResponse({'Error': 'No such article'}, status=404)

	if request.method == 'GET':

		serializer = ArticleSerializer(article)
		return JsonResponse(serializer.data)
	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ArticleSerializer(article, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, 500)

	elif request.method == 'DELETE':
		article.delete()
		return HttpResponse(status=204)
