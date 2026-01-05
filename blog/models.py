from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import get_user_model


# created managers
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class DraftManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.DRAFT)


# Create your models here.

class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DR", 'draft'
        PUBLISHED = "PB", 'published'
        REJECTED = "RJ", 'rejected'

    # relations
    users= models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name="user_post")
    title = models.CharField(max_length=255)
    des = models.TextField()
    slug = models.SlugField()
    puplish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, default=Status.DRAFT, choices=Status.choices)

    objects = models.Manager()
    puplished = PublishedManager()

    objects1 = models.Manager()
    drafted = DraftManager()

    class Meta:
        ordering = ['-puplish']
        indexes = [
            models.Index(fields=['-puplish'])

        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_detail", args=[self.id])
