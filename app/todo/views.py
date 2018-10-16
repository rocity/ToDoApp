from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import ToDoList
from .form import TodoForm


def index(request):
    todo_list = ToDoList.objects.order_by('-id')
    form = TodoForm
    context = {'todo_list': todo_list, 'form': form}
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    if form.is_valid():
        new_todo = ToDoList(todo_text = form.cleaned_data['text'])
        new_todo.save()
    return redirect('index')

def completeTodo(request, todo_id):
    todo = get_object_or_404(ToDoList, id=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')

def delete_completed(request):
    delete_list = ToDoList.objects.filter(completed__exact = True).delete()
    return redirect ('index')

def delete_all(request):
    delete_list = ToDoList.objects.all().delete()
    return redirect('index')
