from django.contrib import admin

# Register your models here.
from .models import Product, SecOne, Video, News

class ProductAdmin(admin.ModelAdmin):
    # admin panel features.
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')

class SecOneAdmin(admin.ModelAdmin):
    # admin panel features.
    list_display = ('name',)
    search_fields = ('name',)

class VideoAdmin(admin.ModelAdmin):
    # admin panel features.
    list_display = ('title',)
    search_fields = ('title',)

class NewsAdmin(admin.ModelAdmin):
    # admin panel features.
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(SecOne, SecOneAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(News, NewsAdmin)