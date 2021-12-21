from django.db import models
from django.utils.translation import gettext_lazy as _

FEED_TYPES = [
    ('rss', 'RSS'),
    ('atom', 'ATOM'),
]


class RssFeedUrl(models.Model):
    website = models.ForeignKey(verbose_name=_('Website'), to='cubansites.Website', on_delete=models.CASCADE)
    url = models.URLField(verbose_name=_('URL'))
    category = models.ForeignKey(verbose_name=_('Category'), to='cubansites.Category',
                                 on_delete=models.SET_NULL, null=True, blank=True)
    feed_type = models.CharField(verbose_name=_('Type'), choices=FEED_TYPES, default='rss', max_length=32)
