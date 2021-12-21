from django.db import models
from django.utils.translation import gettext_lazy as _


class WebCrawler(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=128)
    file_dir = models.FileField(verbose_name=_('File'), upload_to='spiders/uploaded')
