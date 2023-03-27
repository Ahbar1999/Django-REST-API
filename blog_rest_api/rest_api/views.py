from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_api.models import BlogPost
from rest_api.serializers import BlogPostSerializer 


#/all 
@csrf_exempt
def blog_post_list(request):
    if request.method != 'GET':
        return HttpResponse(status=404)
    posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(posts, many=True)
    return JsonResponse(serializer.data, safe=False)

#/create
@csrf_exempt
def create_blog_post(request):
    if request.method == 'GET':
        serializer = BlogPostSerializer(data={})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    return HttpResponse(status=404)

@csrf_exempt
def update_blog_post(request, id):
    if request.method == 'GET':
        return HttpResponse(status=404)
    try:
        blog_post = BlogPost.objects.get(id=id)
    except BlogPost.DoesNotExist: 
        # record does not exist
        return HttpResponse(status=404)
     
    data = JSONParser().parse(request)
    # the 'blog_post' is being passed a 'instance' variable in the update() method 
    serializer = BlogPostSerializer(blog_post, data = data)
    if serializer.is_valid():
        # save the updated blog_post 
        serializer.save()
        return JsonResponse(serializer.data) 
    return HttpResponse(serializer.errors, status=400)