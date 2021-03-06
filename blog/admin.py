from django.contrib import admin
from . models import Category, Post

# for configuration of Ctegory admin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'url', 'add_date')
    search_fields = ('title',)


# for configuration of Post admin


class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'add_date')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
