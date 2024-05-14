from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from .forms import BookForm


def task_list(request):
    query = request.GET.get('query')
    tasks_list = Book.objects.all()

    if query:
        tasks_list = tasks_list.filter(title__icontains=query)

    paginator = Paginator(tasks_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'myfirst.html', {'page_obj': page_obj, 'query': query})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = BookForm()
        return render(request, 'index.html')


def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'myfirst2.html', {'book': book})


from django.shortcuts import get_object_or_404, redirect


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('members')


from django.http import Http404


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('members')
    else:
        form = BookForm(instance=book)
    return render(request, 'index2.html', {'book': book})
