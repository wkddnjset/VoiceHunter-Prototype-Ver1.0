from django.urls import path
from .views import (
    CreateProjectAPI
)

app_name = 'API'
urlpatterns = [
    path('api/add/project/', CreateProjectAPI, name='api-add-project')
]