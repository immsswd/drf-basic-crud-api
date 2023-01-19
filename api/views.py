from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
# django restframework
# from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response
from . serializers import TaskSeliazer
# models
from . models import Task


# api endpoint for Tasks
class TaskList(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSeliazer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSeliazer
    
    def get(self, request, *args, **kwargs):
        instance    = self.get_object()
        serializer  = self.get_serializer(instance)
        return Response(serializer.data)
    
class TaskCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class  = TaskSeliazer

# delete task
# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task        = Task.objects.get(id=pk)
#     task.delete()
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List': '/task-list/',
#         'Detail view': '/task-detail/id/',
#         'Create': '/task-create/',
#         'Update': '/task-update/id/',
#         'Delete': '/task-delete/id/',
#     }
    
#     return Response(api_urls)
    # return JsonResponse("API BASE", safe=False)
    # return HttpResponse("API BASE")
# list all your tasks
# @api_view(['GET'])   
# def taskList(request):
#     tasks       = Task.objects.all()
#     serializer  = TaskSeliazer(tasks, many=True)
#     return Response(serializer.data)

# task detail
# @api_view(['GET'])   
# def taskDetail(request, pk):
#     tasks       = Task.objects.get(id=pk)
#     serializer  = TaskSeliazer(tasks, many=False)
#     return Response(serializer.data)

# create task
# @api_view(['POST'])   
# def taskCreate(request):
#     serializer  = TaskSeliazer(data = request.data)
    
#     if serializer.is_valid():
#         serializer.save()
    
#     return Response(serializer.data)

# update task
# @api_view(['POST'])   
# def taskUpdate(request, pk):
#     task        = Task.objects.get(id=pk)
#     serializer  = TaskSeliazer(instance=task, data = request.data)
    
#     if serializer.is_valid():
#         serializer.save()
    
#     return Response(serializer.data)

# delete task
# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task        = Task.objects.get(id=pk)
#     task.delete()
    
#     return Response("Item sucessfully deleted!")
