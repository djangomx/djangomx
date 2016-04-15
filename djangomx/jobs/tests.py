# coding: utf-8
from django.db import DataError
from django.test import TestCase

from core.utils import truncated_slugify

from .models import Job


class JobTestCase(TestCase):

    def setUp(self):
        self.job = Job.objects.create(title='', contact='me@netoxico.com', content='')
        self.long_title = "Duis mollis, est non commodo luctus, nisi erat \
            porttitor ligula, eget lacinia odio sem nec elit. Lorem ipsum \
            dolor sit amet, consectetur adipiscing elit."

    def test_job_update(self):
        test_title = 'Test job title'
        test_slug = truncated_slugify(test_title)

        self.job.title = test_title
        self.job.save()

        self.assertEqual(self.job.title, test_title)
        self.assertEqual(self.job.slug, test_slug)

    def test_slug_length(self):
        """
        Test for slug length
        """
        self.job.title = self.long_title[:75]
        self.job.save()

        self.assertLessEqual(len(self.job.slug), 75)
        self.assertIsNot(self.job, Job)

    def test_title_length(self):
        """
        Test for title length validation
        """
        # TODO: Handle this somewhere...
        self.job.title = self.long_title

        with self.assertRaises(DataError):
            self.job.save()
