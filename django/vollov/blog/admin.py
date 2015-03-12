from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    #fields = ['posted', 'title']
    list_display = ('title', 'posted', 'slug')
    prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)