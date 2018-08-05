from django.urls import path, include
from .views import (
    HomePage, ProjectListPage
)
from .lang import transLangEN, transLangKO

app_name = 'App'
urlpatterns = [
    path('', HomePage, name='home'),
    path('/projects', ProjectListPage, name='projects'),
]