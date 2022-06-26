import os
import json
from django.core.management.base import BaseCommand
from products.web_scrapers.main import run_scrapers
from django.conf import settings

class Command(BaseCommand):
    help = 'Here we run web scrapers'
    def handle(self, *args, **options):
        run_scrapers()