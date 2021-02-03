from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from .managers import CustomUserManager


class Writer(AbstractUser):
    username = None
    is_editor = models.BooleanField(default=False)
    name = models.CharField(max_length=256, unique=True)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()


class Article(models.Model):
    created_at = models.DateTimeField(verbose_name="Created at",
                                      name="created_at",
                                      default=timezone.now,
                                      blank=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    status = models.TextField(blank=True)
    written_by = models.ForeignKey(Writer,
                                   on_delete=models.CASCADE,
                                   related_name='written_by',
                                   default=None,
                                   blank=True,
                                   null=True)
    edited_by = models.ForeignKey(Writer,
                                  on_delete=models.CASCADE,
                                  related_name='edited_by',
                                  default=None,
                                  blank=True,
                                  null=True)

    APPROVE_CHOICES = (
        ('approve', 'approve'),
        ('reject', 'reject'),
    )
    approve_reject = models.CharField(verbose_name="Approve or reject "
                                                   "an article",
                                      name="approve_reject",
                                      choices=APPROVE_CHOICES,
                                      max_length=128,
                                      default='',
                                      blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.title
