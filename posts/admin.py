from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Main information', {'fields': ['title', 'content']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('title', 'content', 'pub_date')
    list_filter = ['pub_date']
    # Adding search field for the admin panel
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
