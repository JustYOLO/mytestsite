from django.shortcuts import render
from .models import Todo

# 홈페이지 (index.html) 표시
def index(request):
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'index.html', {'todos': todos})

# 새로운 todo 생성
def create_todo(request):
    # Post request를 받음
    title = request.POST.get('title')
    # 받은 이름으로 todo 객체 생성
    todo = Todo.objects.create(title=title)
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    # 저장 후 반환
    return render(request, 'todo-list.html', {'todos': todos})

# 완료한 todo 표시
def mark_todo(request, pk):
    # 해당하는 todo 객체를 가져옴
    todo = Todo.objects.get(pk=pk)
    # 완료로 변경 (추후 toggle로 변경 고려)
    todo.completed = True
    todo.save()
    todos = Todo.objects.all().order_by('-id')
    # 저장 후 반환
    return render(request, 'todo-list.html', {'todos': todos})

# todo를 삭제
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    todos = Todo.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})
