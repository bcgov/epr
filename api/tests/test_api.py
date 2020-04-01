""" Unit tests for API.
"""
import unittest
from unittest.mock import patch

from starlette.testclient import TestClient

from main import APP


class BasicTestCase(unittest.TestCase):
    """ Some basic unit tests. """

    @patch('main.psycopg2')
    def test_health(self, fake_psycopg2):  # pylint: disable=unused-argument
        """ Test that health check returns 200/OK. """
        client = TestClient(APP)
        response = client.get('/health')
        self.assertEqual(response.status_code, 200)
