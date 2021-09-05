import json

from django.shortcuts import render
from django.contrib import messages

from schedule_calendar.forms import TaskCreateForm, TaskEditForm
from schedule_calendar.models import Task


def get_tasks():
    tasks = Task.objects.all()
    if tasks:
        tasks_list = []
        for task in tasks:
            task_dict = {
                "id": task.id,
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
    task_edit_form = TaskEditForm(auto_id="edit_%s")

    if request.POST:
        if request.POST["action"] == "create_task":
            create_form = TaskCreateForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                task_create_form = TaskCreateForm()
            else:
                messages.add_message(
                    request,
                    messages.ERROR,
                    create_form.errors.as_text().split('* ')[-1]
                )
                task_create_form = create_form

        if request.POST['action'] == "edit_task":
            edit_form = TaskEditForm(request.POST)
            if edit_form.is_valid():
                edit_form.save()
                task_edit_form = TaskEditForm(auto_id="edit_%s")
            else:

                task_edit_form = edit_form

    context["task_create_form"] = task_create_form
    context["task_edit_form"] = task_edit_form

    all_tasks = get_tasks()
    context["tasks"] = all_tasks


    return render(request, "home.html", context)