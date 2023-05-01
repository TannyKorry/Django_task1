import csv
from django.core.management.base import BaseCommand
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for itm in phones:
                phone = Phone(
                    id=itm['id'],
                    name=itm['name'],
                    slug=slugify(itm['name']),
                    price=int(itm['price']),
                    image=itm['image'],
                    release_date=itm['release_date'],
                    lte_exists=itm['lte_exists']
                )
                phone.save()
        return

            # TODO: Добавьте сохранение модели
