from django.contrib import admin
from blog.models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["author", 'title', 'content',
                    'status', 'counted_view', "created_date", 'updated_date']
    ordering = ["updated_date"]
    search_fields = ['title', 'content']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    ...
