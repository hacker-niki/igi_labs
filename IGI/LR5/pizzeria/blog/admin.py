from django.contrib import admin

from .models import CompanyInfo, Post, FAQ


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('description',)
    search_fields = ('description',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')
    search_fields = ('title',)
    list_filter = ('published_date',)
    date_hierarchy = 'published_date'


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'added_date')
    search_fields = ('question',)
    list_filter = ('added_date',)
    date_hierarchy = 'added_date'
