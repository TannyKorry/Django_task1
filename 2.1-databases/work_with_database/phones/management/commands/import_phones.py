import csv

from django.core.management.base import BaseCommand
from phones.models import Phone



class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            for itm in phones:
                phone = Phone(
                    id=itm.get('id'),
                    name=itm.get('name'),
                    slug=itm.get('name'),
                    price=int(itm.get('price')),
                    image=itm.get('image'),
                    release_date=itm.get('release_date'),
                    lte_exists=itm.get('lte_exists')
                )
                phone.save()


            # TODO: Добавьте сохранение модели
