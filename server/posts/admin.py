from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'cat',
        'text',
        'date_creation',
        'preview_img'
    )
    ordering = ('id',)

    list_display_links = ('id', 'title')
    list_filter = ('cat','date_creation')
    readonly_fields = ('preview_img', 'img', 'date_creation', 'date_last_modifed')
    search_fields = ('title',)
    date_hierarchy = ('date_creation')
    list_per_page = 10


    def preview_img(self, obj):
        return mark_safe(f'<img src="{obj.preview.url}" style="max-height: 100px; border-radius: 10px"/>')
    preview_img.short_description = 'Превью'

    def img(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 100px; border-radius: 10px"/>')
    img.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('id',)
    list_per_page = 20
    search_fields = ('name',)