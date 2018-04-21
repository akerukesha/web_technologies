from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    done = models.BooleanField(default=False, null=False)

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at.strftime('%m/%d/%Y'),
            'done': self.done,
        }

    def __str__(self):
        return self.title
