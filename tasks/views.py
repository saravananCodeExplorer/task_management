# Import render() to display HTML templates
# Import redirect() to redirect the user to another URL
# Import get_object_or_404() to get an object or return 404 error
from django.shortcuts import render, redirect, get_object_or_404

# Import Task model from models.py
from .models import Task

# Import TaskForm from forms.py
from .forms import TaskForm


# ==========================================
# READ - Display all tasks
# ==========================================
def task_list(request):

    # Get all tasks from the database
    # order_by('-created_at') displays newest tasks first
    tasks = Task.objects.all().order_by('-created_at')

    # Send the tasks to task_list.html
    return render(
        request,
        'tasks/task_list.html',
        {'tasks': tasks}
    )


# ==========================================
# CREATE - Create a new task
# ==========================================
def task_create(request):

    # Check whether the user submitted the form
    if request.method == 'POST':

        # Get submitted form data
        form = TaskForm(request.POST)

        # Validate the form
        if form.is_valid():

            # Save the task into the database
            form.save()

            # Redirect to the task list page
            return redirect('task_list')

    else:

        # Display an empty form for GET request
        form = TaskForm()

    # Display the create task form
    return render(
        request,
        'tasks/task_form.html',
        {
            'form': form,
            'title': 'Create Task'
        }
    )


# ==========================================
# UPDATE - Update an existing task
# ==========================================
def task_update(request, pk):

    # Find the task using its primary key (ID)
    # If the task doesn't exist, return 404 page
    task = get_object_or_404(Task, pk=pk)

    # Check whether the update form was submitted
    if request.method == 'POST':

        # Load submitted data into the existing task
        form = TaskForm(
            request.POST,
            instance=task
        )

        # Validate the form
        if form.is_valid():

            # Update the existing task in the database
            form.save()

            # Redirect to task list
            return redirect('task_list')

    else:

        # Display the existing task data in the form
        form = TaskForm(instance=task)

    # Display update form
    return render(
        request,
        'tasks/task_form.html',
        {
            'form': form,
            'title': 'Update Task'
        }
    )


# ==========================================
# DELETE - Delete an existing task
# ==========================================
def task_delete(request, pk):

    # Find the task using its primary key
    # If task doesn't exist, return 404
    task = get_object_or_404(Task, pk=pk)

    # Check whether delete confirmation was submitted
    if request.method == 'POST':

        # Delete the task from the database
        task.delete()

        # Redirect to task list
        return redirect('task_list')

    # Display delete confirmation page
    return render(
        request,
        'tasks/task_confirm_delete.html',
        {'task': task}
    )