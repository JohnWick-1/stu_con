from .models import StudentCon
from rest_framework.serializers import ModelSerializer

class StudentConSerializer(ModelSerializer):
    class Meta:
        model = StudentCon
        fields = '__all__'
