from django.urls import path
from .views_api import (
    CreateProjectAPI, CreateUserAPI
)

app_name = 'API'
urlpatterns = [
    path('api/add/project/', CreateProjectAPI, name='api-add-project'),
    path('api/signup/', CreateUserAPI, name='api-signup')
]