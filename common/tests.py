import os
from django.test import TestCase
from unittest.mock import patch
from common.utils import get_registered_icons

class GetRegisteredIconsTest(TestCase):

    @patch("os.getcwd")
    @patch("os.path.exists")
    @patch("os.listdir")
    def test_get_registered_icons(self, mock_listdir, mock_exists, mock_getcwd):
        # Set up mock values
        mock_getcwd.return_value = "/mocked/path"
        mock_exists.return_value = True
        mock_listdir.return_value = [
            "activity.html",
            "alert-circle.html",
            "arrow-right.html",
            "non-icon.txt",
        ]

        # Expected output
        expected_icons = [
            "activity",
            "alert-circle",
            "arrow-right"
        ]

        # Call the function and check result
        icons = get_registered_icons("cotton/templates/icons")
        self.assertEqual(icons, expected_icons)

    @patch("os.path.exists")
    def test_directory_does_not_exist(self, mock_exists):
        # Mock directory existence
        mock_exists.return_value = False

        # Call the function and check for empty list
        icons = get_registered_icons("nonexistent/path")
        self.assertEqual(icons, [])