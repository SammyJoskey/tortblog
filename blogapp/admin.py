from django.contrib import admin
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    @staticmethod
    def post_title(obj):
        return obj.post.title

    list_display = ('title', 'category', 'status', 'updated',
                    'publication_date', 'author', )
    fields = ('title', 'category', 'slug', 'author', 'status', 'content',
              'updated', 'publication_date')

    prepopulated_fields = {"slug": ("title",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    @staticmethod
    def category_title(obj):
        return obj.post.name

    list_display = ('cat_title', )
    prepopulated_fields = {"slug": ("cat_title",)}