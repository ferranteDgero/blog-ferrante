from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import Product
from .forms import ProductForm  # Importa el formulario de productos

def home(request):
    return render(request, 'myapp/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'myapp/products.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'myapp/product_detail.html', {'product': product})

# Nueva vista para crear productos
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Acepta datos del formulario y archivos
        if form.is_valid():
            form.save()  # Guarda el producto en la base de datos
            return redirect('product_list')  # Redirige a la lista de productos
    else:
        form = ProductForm()  # Muestra un formulario vacío
    return render(request, 'myapp/create_product.html', {'form': form})