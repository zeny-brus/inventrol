from django.contrib import admin
from .models import Category,Product,Movement



admin.site.register(Product)
admin.site.register(Movement)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
admin.site.register(Category,CategoryAdmin)
