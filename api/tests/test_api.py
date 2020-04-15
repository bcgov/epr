
""" Unit tests for API.
"""
import unittest
from unittest.mock import patch
from starlette.testclient import TestClient
from alchemy_mock.mocking import UnifiedAlchemyMagicMock

from main import APP


class BasicTestCase(unittest.TestCase):
    """ Some basic unit tests. """

    session = UnifiedAlchemyMagicMock()

    test_data = {
        "idir": "employee",
        "status": "Online",
        "location": "Victoria",
        "phone": "123-456-7890"
    }

    @patch('main.SESSION')
    def test_health(self, mock_session):   # pylint: disable=unused-argument
        """ Test that health check returns 200/OK. """
        client = TestClient(APP)
        response = client.get('/health/')
        self.assertEqual(response.status_code, 200)

    @patch('main.SESSION', new=session)
    def test_add_employee(self):
        """ Test that creating an employee returns 200/OK. """
        client = TestClient(APP)
        response = client.post('/employee/',
                               headers={'Content-Type': 'application/json'},
                               json=self.test_data)
        self.assertEqual(response.status_code, 200)

    @patch('main.SESSION', new=session)
    def test_get_employee(self):
        """ Test that fetching an employee returns 200/OK. """
        client = TestClient(APP)
        response = client.get('/employees/{}'.format('employee'))
        self.assertEqual(response.status_code, 200)

    @patch('main.SESSION', new=session)
    def test_get_employees(self):
        """ Test that fetching all employees returns 200/OK. """
        client = TestClient(APP)
        response = client.get('/employees/')
        self.assertEqual(response.status_code, 200)

    @patch('main.SESSION', new=session)
    def test_update_employee(self):
        """ Test that modifying an employee returns 200/OK. """
        client = TestClient(APP)
        response = client.put('/employee/',
                              headers={'Content-Type': 'application/json'},
                              json={
                                  "idir": "employee",
                                  "status": "Offline",
                                  "location": "Victoria",
                                  "phone": "123-456-7890"
                              })
        self.assertEqual(response.status_code, 200)

    @patch('main.SESSION')
    def test_delete_employee(self, mock_session):  # pylint: disable=unused-argument
        """ Test that removing an employee returns 200/OK. """
        client = TestClient(APP)
        response = client.delete('/employees/{}'.format('employee'))
        self.assertEqual(response.status_code, 200)
