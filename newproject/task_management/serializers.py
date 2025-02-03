from rest_framework.serializers import Serializer, ModelSerializer
from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        models=Task
        fields='__all__'