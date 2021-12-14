from django.shortcuts import render
from django.contrib import messages
from .models import Task
from fnmatch import fnmatch
import re
from .forms import TaskForm


# Create your views here.
def index_task(request):
    _put = request.POST.get('_method')
    if request.method == 'POST' and _put == 'PUT':
        param_btn = [name for name in request.POST if fnmatch(name, 'btn*')][0]
        print(param_btn)
        id_ = None
        try:
            rez = re.search(r"\d+", param_btn)
            id_ = rez.group(0)
        except AttributeError as e:
            print(e)
        if id_ is not None:
            t = Task.objects.get(pk=id_)
            t.delete()
            messages.info(request, "Task removed!")

    elif request.method == 'POST':

        # title = request.POST.get('title')
        # priority = request.POST.get('priority')
        # done = True if request.POST.get('complete') == 'on' else False
        # task = Task(title=title, priority=priority, done=done)
        # task.save()
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task add success!")

    tasks = Task.objects.all()
    content = {
        'tasks': tasks
    }

    return render(request, 'taskManagement/index.html', content)
