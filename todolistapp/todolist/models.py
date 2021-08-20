from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=400)
    detail = models.CharField(max_length=400)
    is_completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title