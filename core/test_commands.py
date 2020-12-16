from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase

class CommandTests(TestCase):
    def test_wait_for_db_ready(self):
        with patch('django.db.utils.ConnectionHandler.__getitem__') as get_item:
            get_item.return_value = True
            call_command('wait_for_db')
            self.assertEqual(get_item.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self, time_sleep):
        with patch('django.db.utils.ConnectionHandler.__getitem__') as get_item:
            get_item.side_effect = [OperationalError] * 5 + [True]
            call_command('wait_for_db')
            self.assertEqual(get_item.call_count, 6)
