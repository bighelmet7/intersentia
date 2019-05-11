import unittest

import sqlalchemy
from factories import BarFactory
from intersentia.common import Session
from intersentia.exceptions import ValidationError


class BarTest(unittest.TestCase):

    def setUp(self):
        # Prepare a new clean Session 
        self.session = Session()

    def runTest(self):
        engine = sqlalchemy.create_engine('sqlite://')
        Session.configure(bind=engine)

    def test_email_validation_without_at(self):
        # Having a bad email address:
        bad_email = 'namedomain.com'
        # When creating a Bar model with a bad email this instances shouldnt
        # be committed in the database and raising a ValidationError.
        with self.assertRaises(ValidationError):
            BarFactory(name='BarName', email=bad_email)

    def test_email_validation_bad_domain(self):
        # Having a bad domain address
        bad_domain = 'test@(domain).com'
        # When creating a Bar model with a bad email this instances shouldnt
        # be committed in the database and raising a ValidationError.
        with self.assertRaises(ValidationError):
            BarFactory(name='BarName', email=bad_domain)

    def tearDown(self):
        # Rollback the session, no changes to the database.
        self.session.rollback()
        # Remove it for the nexts tests.
        Session.remove()
