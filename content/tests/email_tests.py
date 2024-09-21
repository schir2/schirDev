from django.core.mail import EmailMessage
from django.test import TestCase
from django.test.utils import override_settings

from core import settings


@override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
class EmailTests(TestCase):
    subject = 'Test Email'
    message = 'This is a test email sent using SMTP in Django <3.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['schir2@gmail.com']

    def test_send_mail(self):
        email = EmailMessage(self.subject, self.message, self.from_email, self.recipient_list)
        email.send(False)


# tests.py


