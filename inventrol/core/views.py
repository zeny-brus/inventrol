from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category,Product

#aplicacao de login
@method_decorator(login_required(login_url='login'), name='dispatch')
def home(request):
    return render(request,'index.html')

def login_view(request):
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
    return render(request, 'login.html',{'form':form})  

def logout_view(request):
    logout(request)
    return redirect('login')

#aplicacao de categoria
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateCategoryView(CreateView):
    model = Category
    template_name = 'categoria/criar_categoria.html'
    fields = ['name']
    success_url = reverse_lazy('list_category')

@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'categoria/criar_categoria.html'
    fields = ['name']
    success_url = reverse_lazy('list_category')
    pk_url_kwarg = 'categoria_id'

@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'categoria/criar_categoria.html'    
    success_url = reverse_lazy('list_category')
    pk_url_kwarg = 'categoria_id'

@method_decorator(login_required(login_url='login'), name='dispatch')
class ListCategoryView(ListView):
    model = Category
    template_name = 'categoria/lista_categoria.html'
    context_object_name = 'categorys'

#aplicacao de produtos
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateProductView(CreateView):
    model = Product
    template_name = 'produto/criar_produto.html'
    fields = ['name','category','description','price','amout', 'min_amout','uni']
    success_url = reverse_lazy('list_product')

@method_decorator(login_required(login_url='login'), name='dispatch')
class ListProductView(ListView):
    model = Product
    template_name = 'produto/lista_produtos.html'
    context_object_name = 'products'

@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateProductView(UpdateView):
    model = Product
    template_name = 'produto/criar_produto.html'
    fields = ['name','category','description','price','amout','min_amout','uni']
    success_url = reverse_lazy('list_product')
    pk_url_kwarg = 'produto_id'

@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteProductView(DeleteView):
    model = Product
    template_name = 'produto/lista_produtos.html'
    success_url = reverse_lazy('list_product')
    pk_url_kwarg = 'product_id'



