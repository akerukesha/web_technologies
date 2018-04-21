from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from contacts.models import Contact


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def contact_list(request):
    if request.method == "GET":
        contacts = Contact.objects.all().order_by('name')
        contacts_json = [contact.to_json() for contact in contacts]
        # return JsonResponse({"todos": todos_json}, safe=False)
        return render(request, 'contact/contact_list.html', {"contact_list": contacts, "active_menu": "contact"})
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def contact_detail(request, contact_id):
    if request.method == "GET":
        if contact_id is None or contact_id is 0:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            contact = Contact.objects.get(id=int(contact_id))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)
        # return JsonResponse({"todo": todo.to_json()}, safe=False)
        return render(request, 'contact/contact_detail.html', {"contact": contact, "active_menu": "contact"})
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def contact_add(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        number = request.POST.get('number', '')
        if name is None or len(name) is 0:
            return JsonResponse({"message": "name format is incorrect"}, status=400)
        if number is None or len(number) is 0:
            return JsonResponse({"message": "number format is incorrect"}, status=400)
        
        new_contact = Contact.objects.create(name=name, number=number)
        return JsonResponse({"contact": new_contact.to_json()}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def contact_change(request):
    if request.method == "POST":
        contact_id = request.POST.get('id', '')
        contact_name = request.POST.get('name', '')
        contact_number = request.POST.get('number', '')
        if contact_id is None or len(contact_id) is 0:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            contact = Contact.objects.get(id=int(contact_id))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        if contact_name is not None and len(contact_name) is not 0:
        	contact.name = contact_name
        if contact_number is not None and len(contact_number) is not 0:
        	contact.number = contact_number
        contact.save()
        return JsonResponse({"contact": contact.to_json()}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def contact_delete(request):
    if request.method == "POST":
        contact_id = request.POST.get('id', '')
        if contact_id is None or len(contact_id) is 0:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            contact = Contact.objects.get(id=int(contact_id))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        contact.delete()
        return JsonResponse({"deleted": True}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)