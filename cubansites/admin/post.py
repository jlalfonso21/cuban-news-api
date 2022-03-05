from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from cubansites.models import Author, Post, Tag

admin.site.register(Author)
admin.site.register(Tag)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "website", "tags_str")
    list_display_links = ("title",)
    list_filter = ("website", "authors")
    list_select_related = True
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ("title", "summary")
    date_hierarchy = "pub_date"
    save_as = False
    save_as_continue = False
    save_on_top = False
    inlines = []

    def tags_str(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])

    tags_str.allow_tags = True
    tags_str.short_description = _("Tags")
