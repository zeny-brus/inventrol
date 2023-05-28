"""
URL configuration for inventrol project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventrol.core.views import home, login_view, logout_view
from inventrol.core.views import (
    CreateCategoryView, 
    UpdateCategoryView, 
    DeleteCategoryView, 
    ListCategoryView,
    create_product,
    update_product,
    ListProductView,
    DeleteProductView,

    )

urlpatterns = [    
    #django admin
    path('admin/', admin.site.urls),
    #urls aplicacao
    path('',home, name='home'),
    path('login/',login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    #categoria
    path('categoria/', ListCategoryView.as_view(), name='list_category'),
    path('categoria/create/', CreateCategoryView.as_view(), name='create_category'),
    path('categoria/<int:categoria_id>/update/', UpdateCategoryView.as_view(), name='update_category'),
    path('categoria/<int:categoria_id>/delete/', DeleteCategoryView.as_view(), name='delete_category'),
    #produto
    path('produto/create/', create_product, name='create_product'),
    path('produto/<int:produto_id>/update/', update_product, name='update_product'),
    path('produto/', ListProductView.as_view(),name='list_product'),    
    path('produto/<int:product_id>/delete/', DeleteProductView.as_view(), name='delete_product')

]
