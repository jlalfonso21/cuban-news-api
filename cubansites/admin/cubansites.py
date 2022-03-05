from django.contrib import admin
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from cubansites.models import Category, RssFeedUrl, WebCrawler, Website

admin.site.register(Category)
admin.site.register(RssFeedUrl)
admin.site.register(WebCrawler)


@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("name", "domain", "url", "update_button")
    list_display_links = ("name",)
    list_filter = ("categories",)
    list_select_related = True
    list_per_page = 100
    list_max_show_all = 200
    list_editable = ()
    search_fields = ("name", "domain")
    save_as = False
    save_as_continue = False
    save_on_top = False

    def update_button(self, obj):
        return mark_safe(
            '<a href="%s" class="button">Actualizar</a>'
            % (
                "asd"
                # reverse_lazy(
                #     "object_details", kwargs={"model_name": "room", "pk": obj.pk}
                # ),
            )
        )

    update_button.allow_tags = True
    update_button.short_description = _("Update")
