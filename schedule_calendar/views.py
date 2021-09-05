import json

from django.shortcuts import render
from django.contrib import messages

from schedule_calendar.forms import TaskCreateForm, TaskEditForm
from schedule_calendar.models import Task
from schedule_calendar.interval_partitioning import find_num_employees


def get_tasks():
    tasks = Task.objects.all()
    tasks_interval_partitioning_format = {}
    tasks_list = []
    if tasks:
        for task in tasks:
            task_dict = {
                "id": task.id,
                "title": task.name,
                "start": task.start_date.strftime('%Y-%m-%dT%H:%M:%SZ'),
                "end": task.end_date.strftime('%Y-%m-%dT%H:%M:%SZ')
            }
            tasks_list.append(task_dict)

            day = task.start_date.strftime('%d/%m/%Y')
            if day not in tasks_interval_partitioning_format:
                tasks_interval_partitioning_format[day] = [
                    tuple([task.name, task.start_date, task.end_date])
                ]
            else:
                tasks_interval_partitioning_format[day].append(
                    tuple([task.name, task.start_date, task.end_date])
                )
    return json.dumps(tasks_list), tasks_interval_partitioning_format


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

    all_tasks, tasks_interval_partitioning_format = get_tasks()

    managed_tasks = []
    for day in tasks_interval_partitioning_format.keys():
        num_employees = find_num_employees(tasks_interval_partitioning_format[day])

        managed_tasks.append(
            {
                'date': day,
                'required_employees': num_employees
            }
        )
    context["tasks"] = all_tasks
    context["managed_tasks"] = managed_tasks


    return render(request, "home.html", context)