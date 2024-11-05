from datetime import datetime
from itertools import groupby
from time import strftime, strptime

from django.http import HttpResponse
from django.shortcuts import render, redirect

from books.models import Book



def index(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    book_list = Book.objects.all()
    print(book_list)
    context = {
        'books': book_list
    }
    return render(request, template, context)


def books_dates(request, pub_date):
    template = 'books/books_filter.html'
    book_list = Book.objects.all().filter(pub_date=pub_date)
    books = Book.objects.all()
    all_dates = [book.pub_date for book in books]
    dis_dates = [ datetime.strftime(dt,'%Y-%m-%d') for dt, _ in groupby(all_dates)]
    if pub_date not in dis_dates:
        return HttpResponse("There is no such page", status=404)
    else:
        cur_index=dis_dates.index(pub_date)
        print(cur_index)
        print(len(dis_dates))
        print(dis_dates)
        if cur_index>0 and cur_index<len(dis_dates)-1:
            date_before = dis_dates[cur_index-1]
            date_after = dis_dates[cur_index+1]
        elif cur_index==0:
            date_before = dis_dates[cur_index]
            date_after = dis_dates[cur_index + 1]
        elif cur_index==(len(dis_dates)-1):
            date_before = dis_dates[cur_index-1]
            date_after = dis_dates[cur_index]
        context = {
            'books': book_list,
            'date_before':date_before,
            'date_after':date_after
        }
        return render(request, template, context)

