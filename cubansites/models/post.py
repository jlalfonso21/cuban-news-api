import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)

    def __str__(self) -> str:
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255)
    slug = models.SlugField(verbose_name=_("Slug"))

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        print(locals())
        return super().save(*args, *kwargs)


class Post(models.Model):
    uuid = models.UUIDField(verbose_name=_("UUID"), default=uuid.uuid4)
    website = models.ForeignKey(to="cubansites.Website", on_delete=models.CASCADE)
    title = models.TextField(verbose_name=_("Title"))
    summary = models.TextField(verbose_name=_("Summary"))
    link = (models.URLField(verbose_name=_("Link")),)
    comments_link = (models.URLField(verbose_name=_("Comments Link")),)
    pub_date = models.DateTimeField(verbose_name=_("Published Date"))
    authors = models.ManyToManyField(to="cubansites.Author", verbose_name=_("Authors"))
    tags = models.ManyToManyField(to="cubansites.Tag", verbose_name=_("Tags"))

    def __str__(self):
        return f"{self.website.name} / {self.title}"
