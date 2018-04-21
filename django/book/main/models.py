from django.db import models


class Author(models.Model):
  name = models.CharField(max_length=200, blank=True)


  def to_json(self):
    return {
        'id': self.id,
        'name': self.name,
    }

  def __str__(self):
    return self.name


class Book(models.Model):
  autor = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
  title = models.CharField(max_length=200, blank=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

  def to_json(self):
    return {
        'id': self.id,
        'title': self.title,
        'updated_at': self.updated_at,
        'created_at': self.created_at,
        'author': self.autor.to_json(),
    }


  def __str__(self):
    return self.title
