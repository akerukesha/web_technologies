from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from api.models import Category, Product


@csrf_exempt
def index(request):
    return render(request, 'index.html')


@csrf_exempt
def all_categories(request):
    if request.method == "GET":
        categories = Category.objects.all().order_by('name')
        categories_json = [c.to_json() for c in categories]
        return render(request, 'categories/categories_list.html', {"categories_list": categories, "active_menu": "category"})
        # return JsonResponse({"categories": categories_json}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)

@csrf_exempt
def category_detail(request, category_id):
    if request.method == "GET":
        if category_id is None:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            category = Category.objects.get(id=int(category_id))
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)
        return render(request, 'categories/categories_detail.html', {"category": category, "active_menu": "category"})
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def new_category(request):
    return render(request, 'categories/categories_add.html')

@csrf_exempt
def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        if name is None or len(name) is 0:
            return JsonResponse({"message": "name format is incorrect"}, status=400)
        
        new_category, _ = Category.objects.get_or_create(name=name)
        return redirect('all_categories')
        # return JsonResponse({"category": new_category.to_json()}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def change_category(request, category_id):
    if category_id is None:
        return JsonResponse({"message": "id format is incorrect"}, status=400)
    try:
        category = Category.objects.get(id=category_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    return render(request, 'categories/categories_edit.html', {"category": category})


@csrf_exempt
def edit_category(request, category_id):
    if request.method == "POST":
        category_name = request.POST.get('name', '')
        if category_id is None:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            category = Category.objects.get(id=category_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        if category_name is not None and len(category_name) is not 0:
            category.name = category_name
        category.save()
        return redirect('all_categories')
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def delete_category(request, category_id):
    if category_id is None:
        return JsonResponse({"message": "id format is incorrect"}, status=400)
    try:
        category = Category.objects.get(id=category_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)

    category.delete()
    return redirect('all_categories')


@csrf_exempt
def all_products(request):
    if request.method == "GET":
        products = Product.objects.all().order_by('name')
        products_json = [p.to_json() for p in products]
        return render(request, 'products/products_list.html', {"products_list": products, "active_menu": "product"})
        # return JsonResponse({"products": products_json}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def product_detail(request, product_id):
    if request.method == "GET":
        if product_id is None:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            product = Product.objects.get(id=product_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)
        return render(request, 'products/products_detail.html', {"product": product, "active_menu": "product"})
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def new_product(request):
    return render(request, 'products/products_add.html')


@csrf_exempt
def add_product(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name', '')
        product_name = request.POST.get('product_name', '')
        price = request.POST.get('price', 0)
        if category_name is None or len(category_name) is 0:
            return JsonResponse({"message": "category_name format is incorrect"}, status=400)
        if product_name is None or len(product_name) is 0:
            return JsonResponse({"message": "product_name format is incorrect"}, status=400)
        if price is None or price is 0:
            return JsonResponse({"message": "price format is incorrect"}, status=400)
        
        print(category_name, product_name, price)
        new_category, _ = Category.objects.get_or_create(name=category_name)
        new_product, _ = Product.objects.get_or_create(name=product_name, price=price, category=new_category)
        return redirect('all_products')
        # return JsonResponse({"product": new_product.to_json()}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def change_product(request, product_id):
    if product_id is None:
        return JsonResponse({"message": "id format is incorrect"}, status=400)
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)
    return render(request, 'products/products_edit.html', {"product": product})


@csrf_exempt
def edit_product(request, product_id):
    if request.method == "POST":
        category_name = request.POST.get('category_name', '')
        product_name = request.POST.get('product_name', '')
        price = request.POST.get('price', 0)

        if product_id is None:
            return JsonResponse({"message": "id format is incorrect"}, status=400)
        try:
            product = Product.objects.get(id=product_id)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=404)

        if category_name is not None and len(category_name) is not 0:
            category, _ = Category.objects.get_or_create(name=category_name)
            product.category = category
        if product_name is not None and len(product_name) is not 0:
            product.name = product_name
        if price is not None and price is not 0:
            product.price = price
        product.save()
        return redirect('all_products')
        # return JsonResponse({"product": product.to_json()}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)


@csrf_exempt
def delete_product(request, product_id):
    if product_id is None:
        return JsonResponse({"message": "id format is incorrect"}, status=400)
    try:
        product = Product.objects.get(id=product_id)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=404)

    product.delete()
    return redirect('all_products')
    # return JsonResponse({"deleted": True}, safe=False)