from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from django.contrib.gis.geos import fromstr, Point, GEOSGeometry
import pandas as pd
from restaurant.models import Restaurant
from django.db.utils import IntegrityError
from decimal import Decimal


class Command(BaseCommand):
    help = 'import data from csv file'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str, help="Path of file")

    def handle(self, *args, **options):
        try:
            path = options['path']
            df = pd.read_csv(path, sep=',')
            restaurants = []
            for index, row in df.iterrows():
                lat, lng = Decimal(row['lat']), Decimal(row['lng'])
                restaurants.append(Restaurant(
                    id=row['id'],
                    rating=row['rating'],
                    name=row['name'],
                    site=row['site'],
                    email=row['email'],
                    phone=row['phone'],
                    street=row['street'],
                    city=row['city'],
                    state=row['state'],
                    location=GEOSGeometry("POINT({0} {1})".format(lng, lat))
,
                ))

            Restaurant.objects.bulk_create(restaurants)
            self.stdout.write(self.style.SUCCESS(
                'Successfully loaded {} records from {}'.format(len(restaurants), path)))
        except IntegrityError:
            self.stdout.write(self.style.ERROR("Data is already loaded"))
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR("File not found"))
        except Exception as e:
            raise e

