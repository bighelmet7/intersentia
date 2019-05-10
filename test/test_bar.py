import unittest
from .common import Session


class BarTest(unittest.TestCase):

    def setUp(self):
        # Prepare a new clean Session 
        self.sesion = Session()

    def test_email_validation(self):
        #TODO: test the raise validator
        pass

    def tearDown(self):
        # Rollback the session, no changes to the database.
        self.session.rollback()
        # Remove it for the nexts tests.
        Session.remove()
