from django.contrib.auth import get_user_model
from django.test import TestCase

from users.models import Profile

User = get_user_model()


class UserProfileTests(TestCase):

    def test_user_creation_creates_profile(self):
        # Create a new user
        user = User.objects.create_user(username='testuser', password='testpass123')

        # Check if the profile is created
        self.assertTrue(Profile.objects.filter(user=user).exists())

    def test_profile_str_method(self):
        # Create a new user
        user = User.objects.create_user(username='testuser', password='testpass123')

        # Check the __str__ method of the profile
        profile = Profile.objects.get(user=user)
        self.assertEqual(str(profile), user.username)

    def test_user_save_updates_profile(self):
        # Create a new user
        user = User.objects.create_user(username='testuser', password='testpass123')

        # Update the user
        user.first_name = 'Test'
        user.save()

        # Check if the profile is still associated with the user
        profile = Profile.objects.get(user=user)
        self.assertEqual(profile.user.first_name, 'Test')
