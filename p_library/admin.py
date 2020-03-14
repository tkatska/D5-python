from django.contrib import admin
from p_library.models import Author, Friend, Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'description', 'year_release',
              'author', 'price', 'copy_count', 'friend')

@admin.register(Friend)
class LibraryAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass