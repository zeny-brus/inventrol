from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category, Product, Movement
from .forms import ProductForm, MovementForm

#aplicacao de login
@login_required(login_url='login')
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
@login_required(login_url='login')
def create_product(request):  
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    else:
        form = ProductForm()
    context = {'form':form}
    return render(request,'produto/criar_produto.html',context)

@login_required(login_url='login')
def update_product(request, produto_id):
    product = get_object_or_404(Product, pk=produto_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list_product')
    else:
        form = ProductForm(instance=product)
    context = {"form":form}
    return render(request, 'produto/criar_produto.html', context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class ListProductView(ListView):
    model = Product
    template_name = 'produto/lista_produtos.html'
    context_object_name = 'products'

@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteProductView(DeleteView):
    model = Product
    template_name = 'produto/lista_produtos.html'
    success_url = reverse_lazy('list_product')
    pk_url_kwarg = 'product_id'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateMovement( LoginRequiredMixin ,CreateView):
    model = Movement
    form_class = MovementForm    
    template_name = 'movimento/lancamento.html'    
    success_url = reverse_lazy('list_movement')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListMovement(ListView):
    model = Movement
    template_name = 'movimento/historico.html'
    context_object_name = 'movements'

class UpdateMovement(LoginRequiredMixin, UpdateView):
    model = Movement
    form_class = MovementForm
    template_name = 'movimento/lancamento.html'
    success_url = reverse_lazy('list_movement')
    pk_url_kwarg = 'movement_id'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)




