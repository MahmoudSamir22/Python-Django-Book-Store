from django.contrib import admin
from .models import Book, Author, Address
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug": ('title',)}
    list_filter = ("author", "title", "rating",)
    list_display = ('title', "author", "rating", 'is_bestselling')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "address")

class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "postal_code", "city")

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Address, AddressAdmin)