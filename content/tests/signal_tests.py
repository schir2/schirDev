from django.core import mail
from django.test import TestCase

from content.models import ContactMessage


class ContactMessageSignalTest(TestCase):
    def test_email_sent_on_contact_message_creation(self):
        mail.outbox = []  # Clear the email outbox

        # Create a new ContactMessage
        contact_message = ContactMessage.objects.create(
            name='John Doe',
            email='john@example.com',
            subject='Test Subject',
            message='This is a test message.'
        )

        # Check that one message has been sent
        self.assertEqual(len(mail.outbox), 1)

        # Verify email content
        email = mail.outbox[0]
        self.assertIn(f'New Message from {contact_message.name} | {contact_message.email}', email.subject)
        self.assertIn('This is a test message.', email.body)
