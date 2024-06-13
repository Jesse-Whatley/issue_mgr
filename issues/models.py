from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

PRIORITIES = [
    ("LO", "Low"),
    ("MD", "Mid"),
    ("HI", "High")
]

COMPLEXITY = [
    (1, "Smallest"),
    (2, "Low mid"),
    (3, "Medium"),
    (5, "Low high"),
    (8, "High"),
    (13, "Very high")
]


class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Issue(models.Model):
    name = models.CharField(max_length=128)
    summary = models.CharField(max_length=256)
    description = models.TextField()
    reporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="reporter"
    )
    assignee = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="assignee"
    )
    complexity = models.IntegerField(
        choices=COMPLEXITY,default=1, 
        blank=True, null=True
        )
    priority = models.CharField(
        max_length=2, choices=PRIORITIES,
        blank=True, null=True
        )
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=0)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("detail", args=[self.id])# detail must be a valid url name later