from django.contrib import admin
from blog.models import Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # list_display = ["user", "title", "des", "status", "created", "puplish"]
    # ordering = ["title", "created"]
    # list_filter = ["status", "puplish"]
    # search_fields = ["title", "des"]
    # # برای نمایش کامل کاربران در پنل ادمین
    # # raw_id_fields = ["author"]
    # date_hierarchy = "puplish"
    # # slug یا برای یوارال پنل ادمین
    # prepopulated_fields = {"slug": ["title"]}
    # list_editable = ["status"]
    # list_display_links = ["title"]
    pass
