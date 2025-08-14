from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("headline", "active", "featured")
    search_fields = ("headline", "sub_headline")
    list_filter = ("active", "featured", "tags")

admin.site.register(Tag)