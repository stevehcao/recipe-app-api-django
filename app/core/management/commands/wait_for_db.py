import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    # customize args and options with *args and **options
    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write('Waiting for database...')
        db_conn = None
        # while it's falsey try to set db connection
        while not db_conn:
            try:
                db_conn = connections['default']
            # if not then sleep for one second
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        # once db is success it'll write this add green style to print to screen
        self.stdout.write(self.style.SUCCESS('Database available!'))