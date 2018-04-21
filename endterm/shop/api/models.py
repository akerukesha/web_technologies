from django.db import models


class Category(models.Model):
    """
    """
    name = models.CharField(max_length=1000, null=False, blank=False,
                                            verbose_name=u"Category name")
    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    class Meta:
        verbose_name = u"Category"
        verbose_name_plural = u"Categories"


class Product(models.Model):
    """
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                                        related_name="products")
    name = models.CharField(max_length=1000, null=False, blank=False,
                                                verbose_name=u"Product name")
    price = models.FloatField(null=False, blank=False,
                                            verbose_name=u"Product price")

    def __str__(self):
        return self.name

    def to_json(self):
        return {
            'id': self.id,
            'category': self.category.to_json(),
            'name': self.name,
            'price': self.price,
        }

    class Meta:
        verbose_name = u"Product"
        verbose_name_plural = u"Products"