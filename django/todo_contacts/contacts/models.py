from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200, blank=True)
    number = models.CharField(max_length=30, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'number': self.number,
            'created_at': self.created_at.strftime('%m/%d/%Y'),
        }

    def __str__(self):
        return self.name
