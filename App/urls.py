from django.urls import path, include
from .views import (
    HomePage, ProjectListPage, ProjectCreatePage
)
from .lang import transLangEN, transLangKO

app_name = 'App'
urlpatterns = [
    path('', HomePage, name='home'),
    path('/projects', ProjectListPage, name='projects'),
    path('/add/project', ProjectCreatePage, name='add-projects'),
]