from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
import jsonfield

def now():
    return timezone.localtime(timezone.now())


class Article(models.Model):

    hash = models.CharField(
        verbose_name=_('Hash'),
        max_length=128,
        blank=True,
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=256,
        blank=True,
    )
    content = models.TextField(
        verbose_name=_('Content'),
        max_length=262144,
        blank=True,
    )
    from_url = models.URLField(
        verbose_name=_('URL'),
        max_length=1024,
        blank=True,
    )
    recommendation = models.BooleanField(
        verbose_name=_('Recommendation'),
        default=False,
    )

    created_by = models.ForeignKey(
        verbose_name=_('Created by'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
    )

    tokenize_output = jsonfield.JSONField(
        verbose_name=_('Tokenize Output'),
        null=True
    )

    ner_output = jsonfield.JSONField(
        verbose_name=_('NER Output'),
        blank=True,
    )

    article_belongto_project = models.ManyToManyField(
        to='project.Project',
        verbose_name=_('Projects'),
        blank=True,
    )

    article_basestone_keyword_sum = models.IntegerField(
        verbose_name=_('Basestone Keyword Amount'),
        blank=True,
        default=0
    )

    article_stellar_keyword_sum = models.IntegerField(
        verbose_name=_('Stellar Keyword Amount'),
        blank=True,
        default=0
    )


    final_output = jsonfield.JSONField(
        verbose_name=_('Final Output'),
        null=True
    )

    def __str__(self):
        return self.name



