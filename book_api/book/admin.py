from django.contrib import admin
from .models import Book, BookSubject
# Register your models here.


class BookInline(admin.TabularInline):
    model = Book
    fields = ["title", "author", "page"]
    extra = 0

class BookSubjectAdmin(admin.ModelAdmin):
    fieldsets= [
        ("Name", {"fields": ["name"]}),
    ]
    inlines=[BookInline]

admin.site.register(BookSubject, BookSubjectAdmin)