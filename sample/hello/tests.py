"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import unittest
from selenium import webdriver
from django.test import TestCase


class SimpleTest(TestCase):
    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.FIREFOX
        desired_capabilities['version'] = '6'
        desired_capabilities['platform'] = 'XP'
        desired_capabilities['name'] = 'Testing Selenium 2 in Python at Sauce'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://azopat:287cc7a1-7ce9-420c-8143-b8c4ee9c2355@ondemand.saucelabs.com:80/wd/hub"
        )

    def test_sauce(self):
        self.driver.get('http://example.saucelabs.com')
        assert "Sauce Labs" in self.driver.title

    def tearDown(self):
        self.driver.quit()

    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)
