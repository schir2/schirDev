# content/signals.py

import logging

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)

from .models import ContactMessage


@receiver(post_save, sender=ContactMessage)
def send_contact_message_email(sender, instance, created, **kwargs):
    if created:
        subject = f'New Message from {instance.name} | {instance.email}'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [settings.EMAIL_HOST_USER]
        context = {
            'contact_message': instance
        }

        text_content = render_to_string('content/emails/contact_message.txt', context=context)
        html_content = render_to_string('content/emails/contact_message.html', context=context)

        msg = EmailMultiAlternatives(subject, text_content, from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        try:
            msg.send()
        except Exception as e:
            logger.error(f'Failed to send email for ContactMessage ID {instance.id}: {e}')
