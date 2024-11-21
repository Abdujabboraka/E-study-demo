from django.urls import path
from .views import *
urlpatterns = [
    # API urls
    path('course/', CourseListAPIView.as_view()),
    path('course/<int:pk>/', CourseListAPIView.as_view()),
    path('student/', StudentView.as_view()),
    path('student/<int:pk>/', StudentView.as_view()),
    path('user/', UserView.as_view()),
    path('user/<int:pk>/', UserView.as_view()),

    # User FRont page urls
    path('', homepage, name='homepage'),
    path('enrollment/', enrollment, name='enrollment'),
    path('detail/<int:course_id>', detail, name='detail'),
    path('register', user_register, name='register'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),

]