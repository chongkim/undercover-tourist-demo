from django.core.management.base import BaseCommand
from django.db import connection

from core.models import ProductListing
from core.api_calls import fetch_product_listing


class Command(BaseCommand):
    def clear_table_sqlite(self):
        cursor = connection.cursor()
        cursor.execute(f'delete from {ProductListing._meta.db_table}')

    def clear_table_mysql(self):
        cursor = connection.cursor()
        cursor.execute(f'truncate table {ProductListing._meta.db_table}')

    def handle(self, **options):
        data = fetch_product_listing()

        if data is None:
            print('error fetching product listing')
            return

        # We're using sqlite right now.  We can use clear_table_mysql() when we switch over
        self.clear_table_sqlite()
        product_listings = ProductListing.objects.bulk_create([ProductListing(**item) for item in data['results']])
        print(f'inserted {len(product_listings)} records')
