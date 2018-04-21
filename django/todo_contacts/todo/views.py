from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser

from todo.models import ToDo
from todo.serializers import ToDoSerializer


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def todo_list(request):
    if request.method == "GET":
        todos = ToDo.objects.all().order_by('-created_at')
        ser = ToDoSerializer(todos, many=True)
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def todo_detail(request, todo_id):
    if request.method == "GET":
        if todo_id is None or todo_id is 0:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            todo = ToDo.objects.get(id=int(todo_id))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)
        ser = ToDoSerializer(todo)
        return JsonResponse(ser.data, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def todo_add(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        ser = ToDoSerializer(data=data)
        if ser.is_valid():
            ser.save()
        return JsonResponse({"todo": ser.data}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def todo_done(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        todo_id = data.get('id', 0)
        print(todo_id)

        if todo_id is None or todo_id is 0:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            todo = ToDo.objects.get(id=todo_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        ser = ToDoSerializer(todo, data)
        if ser.is_valid():
            ser.save()
        return JsonResponse({"todo": ser.data}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def todo_delete(request):
    if request.method == "POST":
        todo_id = request.POST.get('id', '')
        if todo_id is None or len(todo_id) is 0:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            todo = ToDo.objects.get(id=int(todo_id))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        todo.delete()
        return JsonResponse({"deleted": True}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)