from django.contrib import admin
from .models import Category,Product,Movement



admin.site.register(Product)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    
admin.site.register(Category,CategoryAdmin)

class MovementAdmin(admin.ModelAdmin):
    list_display = ('id','product','type_movement','user','date')
admin.site.register(Movement)