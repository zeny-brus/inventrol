from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category

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
class CreateCategoryView(CreateView):
    model = Category
    template_name = 'categoria/criar_categoria.html'
    fields = ['name']
    success_url = reverse_lazy('list_category')

class UpdateCategoryView(UpdateView):
    model = Category
    template_name = 'categoria/criar_categoria.html'
    fields = ['name']
    success_url = reverse_lazy('list_category')
    pk_url_kwarg = 'categoria_id'

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'categoria/criar_categoria.html'    
    success_url = reverse_lazy('list_category')
    pk_url_kwarg = 'categoria_id'

class ListCategoryView(ListView):
    model = Category
    template_name = 'categoria/lista_categoria.html'
    context_object_name = 'categorys'



