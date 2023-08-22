"""
test_send_activation_email_view.py
"""

import unittest
from unittest.mock import patch
from django.contrib.sites.shortcuts import get_current_site
from django.test import RequestFactory
from api.views.send_activation_email_view import SendActivationEmailView


class TestSendActivationEmailView(unittest.TestCase):
    """
    class TestSendActivationEmailView(unittest.TestCase)
    """

    def setUp(self):
        """
        def setUp(self)
        """

        self.uid = "1"
        self.request_factory = RequestFactory()

    @patch("api.views.send_activation_email_view.send_email")
    def test_send_activation_email_view_failure(self, mock_send_email):
        """
        @patch("api.views.send_activation_email_view.send_email")
        def test_send_activation_email_view_failure(self, mock_send_email)
        """

        mock_send_email.return_value = False

        request = self.request_factory.get("/urban_development/send_activation_email/")
        response = SendActivationEmailView.as_view()(request, self.uid)

        self.assertEqual(response.status_code, 200)
        mock_send_email.assert_called_once_with(self.uid,
                                                get_current_site(request).domain,
                                                "Activate your Urban Development account.",
                                                "pages/account_activation_email.html")

    @patch("api.views.send_activation_email_view.send_email")
    def test_send_activation_email_view_success(self, mock_send_email):
        """
        @patch("api.views.send_activation_email_view.send_email")
        def test_send_activation_email_view_success(self, mock_send_email)
        """

        mock_send_email.return_value = True

        request = self.request_factory.get("/urban_development/send_activation_email/")
        response = SendActivationEmailView.as_view()(request, self.uid)

        self.assertEqual(response.status_code, 200)
        mock_send_email.assert_called_once_with(self.uid,
                                                get_current_site(request).domain,
                                                "Activate your Urban Development account.",
                                                "pages/account_activation_email.html")
