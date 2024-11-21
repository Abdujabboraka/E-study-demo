from rest_framework.serializers import ModelSerializer
from .models import Users, Course, Student


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"