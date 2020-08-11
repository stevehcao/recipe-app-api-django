# mocking tests
# so you don't rely on external services
from unittest.mock import patch

# stimulate calling db and seeing if it's available
from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available"""

        # need to mock when db is connected and available
        # operational db
        # mock connection handler grabbing db
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    # here using patch as decorator is similar to with patch(...)
    # pass return value as part of function call
    # except pass in as argument in function, in example as ts
    # above it was as gi
    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # sideffect to test
            # raise op error 5 times
            gi.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)


