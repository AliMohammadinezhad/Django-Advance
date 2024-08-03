from django.contrib import admin


from .models import Post, Category


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "author",
        "title",
        "category",
        "status",
        "created_date",
        "published_date",
    ]
    list_editable = ["status"]
    list_per_page = 10
    list_filter = ["category"]
    search_fields = ["title", "author", "content"]
    date_hierarchy = "created_date"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
