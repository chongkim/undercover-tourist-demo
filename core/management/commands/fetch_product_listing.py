from pprint import pprint
import json

import requests

from django.core.management.base import BaseCommand
from django.db import connection

from core.models import ProductListing


class Command(BaseCommand):
    def handle(self, **options):
        response = requests.get('https://careers.undercovertourist.com/assignment/1/products/', headers={
            'X-Auth': 'chong.kim',
        })

        cursor = connection.cursor()
        # Use this for postgres or mysql
        # cursor.execute(f'truncate table {ProductListing._meta.db_table}')
        # doing a delete with no where clause will do a truncate table for sqlite
        cursor.execute(f'delete from {ProductListing._meta.db_table}')


        data = json.loads(response.text)
        ProductListing.objects.bulk_create([ProductListing(**item) for item in data['results']])
