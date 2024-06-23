from django.contrib import admin

from .models import Note, Author, Category

admin.site.register(Note)
admin.site.register(Author)
admin.site.register(Category)
