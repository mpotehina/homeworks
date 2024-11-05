import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            lte_convert = True
            #if phone['lte_exists'] == 'True':
            #    lte_convert = True
            #elif phone['lte_exists'] == 'False':
            #    lte_convert = False
            #print(datetime.strptime(phone['release_date'], '%Y-%m-%d'))

            model = Phone(id=phone['id'], name=phone['name'], image=phone['image'], price=phone['price'],
                          release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d'), lte_exists=lte_convert)
            model.save()
            pass
