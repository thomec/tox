# rango/admin.py


from django.contrib import admin

from rango.models import Category, Page



class PageTabInline(admin.TabularInline):
    model = Page
    extra = 1


class CategoryAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Name', {'fields': ['name', 'slug']}),
        ('Stats', {'fields':['views', 'likes']}),
    ]
    prepopulated_fields = {'slug':('name',)}
    inlines = [PageTabInline]
    

class PageAdmin(admin.ModelAdmin):
    fields = ['category', 'title', 'url', 'views']
    list_display = ('title', 'category', 'url')



admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

# Register your models here.
