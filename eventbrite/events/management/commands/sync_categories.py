import requests
from django.core.management.base import BaseCommand, CommandError
from events.models import Category


class Command(BaseCommand):
    args = ''
    help = 'Call EventbriteAPI to get category data'

    def handle(self, *args, **options):
        resp = requests.get("https://www.eventbriteapi.com/v3/categories/?token=BKKRDKVUVRC5WG4HAVLT")
        if resp.status_code == 200:
            resp_json = resp.json()
            pagination = resp_json['pagination']
            categroy_list = resp_json['categories']
            for category in categroy_list:
                Category.objects.create(cid=category['id'],
                                        name=category['name'],
                                        name_localized=category['name_localized'],
                                        short_name=category['short_name'],
                                        short_name_localized=category['short_name_localized'],
                                        uri=category['resource_uri'])
            self.stdout.write('Successfully get categories data from API')

        else:
            raise CommandError('Something is wrong with Eventbrite API')
