from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Note(models.Model):
    PRIORITY_CHOICES = (
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(blank=True, null=True)
    alarm_time = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    is_completed = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default="low")
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"Note: {self.title} - {self.image}"

    def get_absolute_url(self):
        return reverse("note_detail", args=[str(self.id)])

    def build_url(self):
        return f"/note/{self.id}/"

    def is_overdue(self):

        return self.due_date and self.due_date < timezone.now()

    def is_in_trash(self):

        return self.deleted_at is not None

    def permanently_delete_after_7_days(self):

        if self.deleted_at:
            return self.deleted_at + timedelta(days=7) <= timezone.now()

    def restore(self):

        self.deleted_at = None
        self.save()


@receiver(post_save, sender=Note)
def auto_delete_notes(sender, instance, **kwargs):

    if instance.is_in_trash() and instance.permanently_delete_after_7_days():
        instance.delete()
