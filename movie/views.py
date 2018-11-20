from django.shortcuts import render,redirect
from .models import Customer,Movie
from .forms import CustomerForm,MovieForm

# Create your views here.
def home(request):
    return render(request,"home.html",context=None)

def addmovie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('availablemovie')
    else:
        form=MovieForm(None)
    return render(request, 'movieinfo.html', {'form': form})

def addcustomer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('availablemovie')
    else:
        form=CustomerForm(None)
    return render(request, 'customerinfo.html', {'form': form})


def availablemovie(request):
    movie_result = Movie.objects.filter(assigncustomer=None).order_by('moviename')
    context = {'movie_result': movie_result}
    return render(request, 'availablemovie.html', context)


def rentedmovie(request):
    moviename = Movie.objects.filter(assigncustomer__isnull=False).order_by('moviename')
    context = {'moviename': moviename}
    return render(request, 'rentedmovie.html', context)

def update(request, movieid):
    if request.method == 'POST':
        object = Movie.objects.get(id=movieid)
        object.assigncustomer = None
        object.save()
        return redirect('availablemovie')

def assignmovie(request):
    moviename = Movie.objects.filter(assigncustomer__isnull = True).order_by('moviename')
    customername = Customer.objects.all()

    if request.method == 'POST':
        selected_movie = request.POST['movie']
        selected_customer = request.POST['customer']
        movie = Movie.objects.get(id = selected_movie)
        customer = Customer.objects.get(id = selected_customer)
        movie.assigncustomer=customer
        movie.save()
        return redirect('rented')

    context = {'moviename': moviename, 'customername': customername}
    return render(request, 'assignmovie.html', context)


def listofcustomer(request):
    customer_result = Customer.objects.all().order_by("first")
    context = {'customer_result': customer_result}
    return render(request, 'customerdata.html', context)


def listofmovie(request):
    movie_result = Movie.objects.all().order_by("moviename")
    context = {'movie_result': movie_result}
    return render(request, 'moviedata.html', context)

def deletemovie(request, delete_movieid):
    if request.method == 'POST':
        object = Movie.objects.filter(id=delete_movieid)
        object.delete()
        return redirect('availablemovie')

def deletecust(request, delete_custid):
    if request.method == 'POST':
        object = Customer.objects.filter(id=delete_custid)
        object.delete()
        return redirect('listofcustomer')