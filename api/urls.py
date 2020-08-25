from django.conf.urls import url
from django.urls import path
from .views import UsersHandler, UsersDetails, UsersCheck, TodoHandler

urlpatterns = [
    path('api/v1/users', UsersHandler.as_view()),
    path('api/v1/users/<int:id>/', UsersDetails.as_view()),
    path('api/v1/users/<str:username>&<str:password>/', UsersCheck.as_view()),
    path('api/v1/users/<int:id>/todos', TodoHandler.as_view()),
    # path('', views.home, name="home"),
]
