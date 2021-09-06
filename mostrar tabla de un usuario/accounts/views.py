from accounts.decorators import unaunthenticated_user
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import Group


from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

#creaciones de las vistas
from .forms import CreateUserForm
from .decorators import unaunthenticated_user,allowed_user
from .models import *
from .filters import orderFilter


def home(request):
    return render(request,'home.html')



def registerPage(request):
    form = CreateUserForm()
    
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user =form.save()
            username = form.cleaned_data['username']
            group = Group.objects.get(name='prueba')
            user.groups.add(group)

            messages.success(request, 'la carga ha sido exitosa' + ' ' + username)
            return redirect('login')

    context ={'form':form}
    return render(request,'register.html',context)



def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'el usuario o la contra, son invalidos')
            
    context ={}

    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_user(allowed_roles=['admin', 'prueba'])
def estadisticas(request):

    orders = order.objects.all()
    costumers = costumer.objects.all()
    total_orders = orders.count()
    pending= orders.filter(status='Pending').count()
    delivered= orders.filter(status='Delivered').count()

    context = {'orders':orders, 'costumers':costumers, 'total_orders':total_orders, 'pending':pending, 'delivered':delivered }

    return render(request,'estadisticas.html',context)

@login_required(login_url='login')
def productos(request):
    context = product.objects.all()
    return render(request,'productos.html',{'products':context})

@login_required(login_url='login')

def customers(request,pk_test):
    
    costum=costumer.objects.get(id=pk_test)

    orders=costum.order_set.all()
    total_orders= orders.count()

    myfilter=orderFilter(request.GET,queryset=orders)
    orders= myfilter.qs

    context = {'costumer':costum, 'orders':orders,'total_orders':total_orders,'myfilter':myfilter }

    return render(request,'costumer.html',context)


