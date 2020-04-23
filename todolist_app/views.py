from django.shortcuts import render, redirect
from django.http import HttpResponse
from todolist_app.models import TaskList
from todolist_app.forms import TaskForm
from django.contrib import messages 
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def todolist(request):
	
	if request.method == 'POST':
		form = TaskForm(request.POST or None)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.owner = request.user
			instance.save()
			
		messages.success(request,('New task added'))
		return redirect('todolist')
	
	else:
			# take all object of class 
			all_tasks = TaskList.objects.filter(owner=request.user)
			paginator = Paginator(all_tasks, 10)
			page = request.GET.get('pg')
			all_tasks = paginator.get_page(page)

			return render(request, 'todolist.html', {'all_tasks': all_tasks})

@login_required
def delete_task(request, task_id):
	task = TaskList.objects.get(pk=task_id)
	if task.owner == request.user:
		task.delete()
	else:
		messages.error(request,('Access restricted. You are not allowed to view this task'))
	return redirect('todolist')

@login_required
def complete_task(request, task_id):
	task = TaskList.objects.get(pk=task_id)
	if task.owner == request.user:
		task.done = True
		task.save()
	else:
		messages.error(request,('Access restricted. You are not allowed to view this task'))

	return redirect('todolist')


@login_required
def pending_task(request, task_id):
	task = TaskList.objects.get(pk=task_id)
	task.done = False
	task.save()
	return redirect('todolist')

@login_required
def edit_task(request, task_id):
	
	if request.method == 'POST':
		task = TaskList.objects.get(pk=task_id)
		form = TaskForm(request.POST or None, instance = task)
		if form.is_valid():
			form.save()

		messages.success(request,('Task edited. '))
		return redirect('todolist')
	
	else:
			# take the onject we want to edit
			task_obj = TaskList.objects.get(pk=task_id)
			return render(request, 'edit.html', {'task_obj': task_obj})


def index(request):
	return render(request, 'index.html', {})


def about(request):
	my_name = "Hola a todos, me llamo Pavel Fernandez Garcia "
	return render(request, 'about.html', {'my_stuff' : my_name})

@login_required
def contactus(request):
	return render(request, 'contactus.html', {})