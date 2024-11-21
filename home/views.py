from django.shortcuts import render, redirect
from .forms import EnrollForm, Registration, LoginForm
from .models import Course, Student, Users
from django.contrib.auth import login, logout
from django.contrib import messages
from .serializer import CourseSerializer, StudentSerializer, UserSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly

class CourseListAPIView(APIView):
    # rest framework permissions
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, pk=None):
        if pk:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request: Request, pk: int):
        course = Course.courses.get(pk=pk)
        serializer = CourseSerializer(course, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk:int):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response(201)



class StudentView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    def get(self, request: Request, pk=None):
        if pk:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request: Request, pk: int):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk:int):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(201)



class UserView(APIView):
    permission_classes = [IsAdminOrReadOnly]
    def get(self, request: Request, pk=None):
        if pk:
            user = Users.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


    def post(self, request: Request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request: Request, pk: int):
        user = Users.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request: Request, pk: int):
        user = Users.objects.get(pk=pk)
        user.delete()
        return Response(201)





























# Create your views here.
def homepage(request):

    return render(request, 'index.html', {'courses': Course.objects.all()})

def detail(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'course.html', {'course': course})


def enrollment(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            course = form.cleaned_data.get('course')
            student.course.add(course)
            return redirect('homepage')
    else:
        form = EnrollForm()

    return render(request, 'enroll.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')
    else:
        form = Registration()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Muvafaqiyatli Login')
            return redirect('homepage')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def user_logout(request):
        logout(request)
        messages.success(request, 'Muvafaqiyatli Logout')
        return redirect('homepage')