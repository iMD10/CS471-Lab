from django.shortcuts import render ,redirect
from .models import Book, Publisher, Author
from django.db.models import Q, Sum, Max, Min, Count, Avg

# def index(request):
#   name = request.GET.get("name") or "world!"
#   return render(request, "bookmodule/index.html", {"name": name}) 

# def index2(request, val1 = 0):
#   if type(val1) is not int:
#     return
#   return render(request,"bookmodule/index2.html", {"val1": val1} )

# def viewbook(request, bookId):
#  # assume that we have the following books somewhere (e.g. database)
#  book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
#  book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
#  targetBook = None
#  if book1['id'] == bookId: targetBook = book1
#  if book2['id'] == bookId: targetBook = book2
#  context = {'book':targetBook} # book is the variable name accessible by the template
#  return render(request, 'bookmodule/show.html', context)


def index(request):
 return render(request, "bookmodule/index.html")
def list_books(request):
 return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def viewlinks(request):
 return render(request, 'bookmodule/links.html')

def texts(request):
 return render(request, 'bookmodule/texts.html')

def listing(request):
 return render(request,'bookmodule/listing.html')

def tables(request):
 return render(request,'bookmodule/tables.html')

def search(request):

  if request.method == "POST":
    string = request.POST.get('keyword').lower()
    isTitle = request.POST.get('option1')
    isAuthor = request.POST.get('option2')
    # now filter
    books = __getBooksList()
    newBooks = []
    for item in books:
      contained = False
      if isTitle and string in item['title'].lower(): contained = True
      if not contained and isAuthor and string in item['author'].lower():contained = True

      if contained: newBooks.append(item)
    return render(request, 'bookmodule/bookList.html', {'books':newBooks})
  return render(request, 'bookmodule/form.html')

def __getBooksList():
  book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
  book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
  book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
  return [book1, book2, book3]


# def simple_query(request):
#   myBooks = Book.objects.filter(title__icontains='and')
#   return render(request, 'bookmodule/bookList.html', {'books':myBooks})

# def complex_query(request):
#   mybooks = Book.objects.filter(author__isnull=False).filter(title__icontains='and').filter(edition__gte = 1).exclude(price__lte = 50)[:10]
#   if len(mybooks)>= 1:
#    return render(request, 'bookmodule/bookList.html', {'books': mybooks})
#   else:
#    return render(request, 'bookmodule/index.html')
  

# def task1(request):
#   books = Book.objects.filter(Q(price__lte=80))
#   return render(request, 'bookmodule/bookList.html', {'books':books})

# def task2(request):
#   books = Book.objects.filter(Q(edition__gt=2) & (Q(author__contains='qu') | Q(title__contains='qu')))

#   return render(request, 'bookmodule/bookList.html', {'books':books})

# def task3(request):
#   books = Book.objects.filter(~Q(edition__gt=3) & (~Q(author__contains='qu') | ~Q(title__contains='qu')))

#   return render(request, 'bookmodule/bookList.html', {'books':books})

# def task4(request):
#   books = Book.objects.filter().order_by('title')

#   return render(request, 'bookmodule/bookList.html', {'books':books})

# def task5(request):
#   sum = Sum('price', default= 0)
#   average = Avg('price', default=0) 
#   max = Max('price', default=0)
#   min = Min('price', default=0)

#   info = Book.objects.aggregate(Count('title'),sum,average,max,min)
  
#   return render(request, 'bookmodule/bookStat.html', {'info':info})

# def task7(request):

#   info = Student.objects.values('address__city').annotate(count = Count('id'))
  
#   return render(request, 'bookmodule/studnets.html', {'info':info})

def task1(request):
 total_books = Book.objects.aggregate(sum = Sum('quantity'))['sum']
 books = Book.objects.all()

 for b in books:
    b.percentage = round(b.quantity / total_books * 100,2) 
 return render(request, 'bookmodule/bookLab9.html', {'info':books, 'total':total_books})


def task2(request):
 count_books = Publisher.objects.annotate(count = Sum("book__quantity"))

 return render(request, 'bookmodule/publishers.html', {'info':count_books})

 
def task3(request):
 
 publishers_books = Publisher.objects.annotate(old= Min("book__pubdate"))
 for i in publishers_books:
  old_book = Book.objects.filter(publisher = i, pubdate = i.old).first()
  i.oldest = old_book

 return render(request, 'bookmodule/pubOld.html', {'info':publishers_books})

def task4(request):
 
 publishers_books = Publisher.objects.annotate(max = Max('book__price'), min = Min('book__price'), avg = Avg('book__price'))
 

 return render(request, 'bookmodule/pubBook.html', {'info':publishers_books})

def task5(request):
 
 highly_rated = Count("book", filter=Q(book__rating__gt = 3))


 publishers_books = Publisher.objects.annotate(high_books = highly_rated)

 for i in publishers_books:
  i.rated = Book.objects.filter(publisher=i, rating__gt = 3)
 return render(request, 'bookmodule/ratedBooks.html', {'info':publishers_books})

def task6(request):
 
 expensive = Count("book", filter=Q(book__price__gt = 50) & (Q(book__quantity__lt = 5) & Q(book__quantity__gte = 1) ))

 publishers_books = Publisher.objects.annotate(expensive_books = expensive)

 return render(request, 'bookmodule/lab9Task6.html', {'info':publishers_books})


def CRUD_list_books(request):
  books = Book.objects.all()
  return render(request,'bookmodule/bookListCRUD.html',{'books':books})


def CRUD_add_book(request):
 authors = Author.objects.all()
 publisher = Publisher.objects.all() 
 if request.method == 'POST':
  title = request.POST.get('title')
  price = request.POST.get('price')
  pubdate = request.POST.get('pubdate')
  quantity = request.POST.get('quantity')
  pub_id = request.POST.get('publisher')
  pub_obj = Publisher.objects.get(id = pub_id)
  
  obj = Book(title= title, price = price, quantity= quantity, pubdate = pubdate)
  
  obj.save()
  obj.publisher = pub_obj
  obj.save()
  authors_ids = request.POST.getlist('authors')
  obj.authors.set(authors_ids)
  return redirect('books.lab10.listbooks')
 return render(request,'bookmodule/addBook.html', {'authors': authors, 'publisher': publisher})


def CRUD_edit_book(request, bid):
 obj = Book.objects.get(id = bid)
 if request.method == 'POST':
  title = request.POST.get('title')
  price = request.POST.get('price')
  pubdate = request.POST.get('pubdate')
  quantity = request.POST.get('quantity')

  obj.title = title
  obj.price = price
  obj.quantity = quantity
  obj.pubdate = pubdate
  obj.id = bid
  obj.save()
  return redirect('books.lab10.listbooks')
 return render(request,'bookmodule/editBook.html', {'book': obj})


def CRUD_delete_book(request, bid):
    book = Book.objects.get(id=bid)
    book.delete()
    return redirect('books.lab10.listbooks')
