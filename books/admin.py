from django.contrib import admin
from .models import Book
# Register your models here.
# admin.site.register(Book)

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('status',"id", "name")