from django.contrib import admin
from .models import Category, Script

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    search_fields  = ('name',)


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_at')
    list_filter =('category' , 'created_at')
    search_fields = ('title','description','code')
    
     
