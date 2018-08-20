from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.shortcuts import render
from .forms import ProjectForm
from .models import *

# Create your views here.
def HomePage(request):
    projects = Project.objects.all()

    item_list = []
    for project in projects[:6]:
        dict = {}
        dict['project'] = project
        dict['apply'] = len(ProjectApply.objects.filter(project=project))
        dict['tags'] = ProjectTag.objects.filter(project=project)[:3]
        item_list.append(dict)
    return render(request, 'Home/HomePage.html', {
        'items':item_list,
    })

def ProjectListPage(request):
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

    paginator = Paginator(item_list, 3)
    contacts = paginator.get_page(page)

    return render(request, 'ProjectList/ProjectListPage.html', {
        'search': search,
        'page': page,
        'items': contacts,
        'projects_len':len(projects),
    })

def ProjectCreatePage(request):

    if request.method == "POST":
        form = ProjectForm(request.POST)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
        return redirect('App:detail-projects', pk=post.id)
    else:
        form = ProjectForm()

    tags = Tag.objects.all()
    return render(request, 'ProjectCreate/ProjectCreatePage.html', {
        'form': form,
        'tags': tags
    })

def ProjectDetailPage(request, pk):

    project = Project.objects.get(pk=pk)
    item = {}
    item['project'] = project
    item['apply'] = len(ProjectApply.objects.filter(project=project))
    item['tags'] = ProjectTag.objects.filter(project=project)[:6]

    return render(request, 'ProjectDetail/ProjectDetailPage.html', {
        'item':item,
    })

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'