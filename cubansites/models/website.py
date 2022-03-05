from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=128)

    def __str__(self) -> str:
        return self.name


class Website(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    domain = models.CharField(verbose_name=_("Domain"), max_length=255)
    url = models.URLField(verbose_name=_("URL"))
    categories = models.ManyToManyField(
        verbose_name=_("Categories"), to="cubansites.Category", related_name="websites"
    )

    def __str__(self) -> str:
        return self.name
