from django.db import models
from slugify import slugify


class Phone(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=150)

    # TODO: Добавьте требуемые поля

    def __str__(self):
        return f'{self.name}, {self.price}, {self.image}'

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __repr__(self):
        return f'{self.name}, {self.price}, {self.image}'




