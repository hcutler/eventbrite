import requests
from .models import Category


def migrate_categories():
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
                                    uri=category['resource_uri']
            )

if __name__ == "__main__":
    migrate_categories()