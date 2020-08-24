from django.urls import path
from .views import UsersHandler, UsersDetails

urlpatterns = [
    path('api/v1/users/', UsersHandler.as_view()),
    path('api/v1/users/<int:id>/', UsersDetails.as_view()),
    # path('', views.home, name="home"),
]
