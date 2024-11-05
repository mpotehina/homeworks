from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    image = models.CharField(max_length=500)
    price = models.CharField(max_length=100)
    release_date = models.CharField(max_length=50)
    lte_exists = models.CharField(max_length=10)
    slug = models.SlugField()

    pass


    def __str__(self):
        return f'{self.id}, {self.name}: {self.price}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
