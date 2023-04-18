from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.TextField()
    release_date = models.CharField(max_length=20)
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=150)

    # TODO: Добавьте требуемые поля

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
