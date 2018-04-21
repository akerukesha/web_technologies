from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from main.models import Book, Author


def index(request):
  return render(request, 'index.html')


def books_list(request):
  books = Book.objects.all().order_by('-created_at')
  return render(request, 'book/book_list.html', {"book_list": books, "active_menu": "book"})


def books_details(request, book_id):
  book = Book.objects.get(pk=book_id)
  return render(request, 'book/book_details.html', {"book": book, "active_menu": "book"})


def authors_list(request):
  authors = Author.objects.all()
  return render(request, 'author/author_list.html', {"author_list": authors, "active_menu": "author"})


def authors_details(request, author_id):
  author = Author.objects.get(pk=author_id)
  return render(request, 'author/author_details.html', {"author": author, "active_menu": "author"})

@csrf_exempt
def books_add(request):
    if request.method == "POST":
        title = request.POST.get('title', '')
        author = request.POST.get('author', '')
        if title is None or len(title) is 0:
            return JsonResponse({"message": "title format is incorrect"}, status=400)
        if author is None or len(author) is 0:
            return JsonResponse({"message": "author format is incorrect"}, status=400)
        
        author, _ = Author.objects.get_or_create(name=author)
        book, _ = Book.objects.get_or_create(title=title, autor=author)
        return JsonResponse({"book": book.to_json()}, safe=False)
    else:
        return JsonResponse({"message": "wrong request type"}, status=400)