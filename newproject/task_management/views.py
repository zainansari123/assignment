from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task 
from rest_framework.request import Request

# Create your views here.
class TaskManagement(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task created successfully', 'data': serializer.data}, status=201)
        return Response({'message': 'Failed to create task', 'errors': serializer.errors}, status=400)

    def get(self, request, format=None):
        try:
            task_id = request.query_params.get('task_id')  # Correct way to get query params
            if not task_id:
                return Response({'message': 'task_id is required'}, status=400)

            tasks = Task.objects.filter(task_id=task_id)
            if tasks.exists():
                data = TaskSerializer(tasks, many=True).data
                return Response({'message': 'Tasks fetched successfully', 'data': data}, status=200)
            return Response({'message': 'No tasks found'}, status=404)
        
        except Exception as e:
            return Response({'message': 'An error occurred', 'error': str(e)}, status=500)