from django.core.management.base import BaseCommand
import os
import MySQLdb as mdb

class Command(BaseCommand):
    help = 'Before web scraping you need to empty the json and the media/products folder'
    def handle(self, *args, **options):
        filePath = 'output.json'
        if os.path.exists(filePath):
            os.remove(filePath)
        else:
            pass
        with open(os.path.join('output.json'), 'w') as json_file:
            pass
        dir = os.path.join('media/products')
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))