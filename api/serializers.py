# which models to serialze?
from rest_framework import serializers
from . models import Task

class TaskSeliazer(serializers.ModelSerializer):
    class Meta:
        model       = Task
        fields      = '__all__'