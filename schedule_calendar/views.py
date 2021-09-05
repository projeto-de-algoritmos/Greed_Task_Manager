import json

from django.shortcuts import render

from schedule_calendar.forms import TaskCreateForm
from schedule_calendar.models import Task


def get_tasks():
    tasks = Task.objects.all()
    if tasks:
        tasks_list = []
        for task in tasks:
            task_dict = {
                "title": task.name,
                "start": task.start_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "end": task.end_date.strftime('%Y-%m-%dT%H:%M:%SZ')
            }
            tasks_list.append(task_dict)
    else:
        tasks_list = []
    return json.dumps(tasks_list)


def home_view(request):
    context = {}
    task_create_form = TaskCreateForm()

    if request.POST:
        if request.POST["action"] == "create_event":
            form = TaskCreateForm(request.POST)
            if form.is_valid():
                form.save()
                task_create_form = TaskCreateForm()
            else:
                task_create_form = form

    context["task_create_form"] = task_create_form
    all_tasks = get_tasks()
    context["tasks"] = all_tasks

    return render(request, "home.html", context)