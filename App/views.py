from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.utils import translation
from .models import *
# Create your views here.
def HomePage(request, lang='ko'):
    translation.activate(lang)
    projects = Project.objects.all()

    item_list = []
    for project in projects[:6]:
        dict = {}
        dict['project'] = project
        dict['apply'] = len(ProjectApply.objects.filter(project=project))
        dict['tags'] = ProjectTag.objects.filter(project=project)[:3]
        item_list.append(dict)
    return render(request, 'Home/HomePage.html', {
        'lang':lang,
        'items':item_list,
    })

def ProjectListPage(request, lang='ko'):
    translation.activate(lang)
    search = request.GET.get('q')
    page = request.GET.get('page')
    if search == None:
        search = ""
    if page == None:
        page = 1

    projects = Project.objects.all()
    item_list = []
    for project in projects:
        dict = {}
        dict['project'] = project
        dict['apply'] = len(ProjectApply.objects.filter(project=project))
        dict['tags'] = ProjectTag.objects.filter(project=project)[:6]
        item_list.append(dict)

    paginator = Paginator(item_list, 1)
    contacts = paginator.get_page(page)

    return render(request, 'ProjectList/ProjectListPage.html', {
        'lang': lang,
        'search': search,
        'page': page,
        'items': contacts,
        'projects_len':len(projects),
    })

def ProjectCreatePage(request, lang='ko'):
    translation.activate(lang)
    return render(request, 'ProjectCreate/ProjectCreatePage.html', {
        'lang': lang
    })

def ProjectDetailPage(request, pk, lang='ko'):
    translation.activate(lang)

    project = Project.objects.get(pk=pk)
    item = {}
    item['project'] = project
    item['apply'] = len(ProjectApply.objects.filter(project=project))
    item['tags'] = ProjectTag.objects.filter(project=project)[:6]

    return render(request, 'ProjectDetail/ProjectDetailPage.html', {
        'lang': lang,
        'item':item,
    })