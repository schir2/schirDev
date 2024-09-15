from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox

from content.models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    SUBJECT_CHOICES = [
        ('contract', 'Contract Work'),
        ('full_time', 'Full-Time Opportunity'),
        ('general_inquiry', 'General Inquiry'),
    ]

    name = forms.CharField(
        label="Full Name",
        help_text="Please enter your full name or the name of your organization.",
        widget=forms.TextInput(attrs={'placeholder': 'Full Name or Organization Name'})
    )
    email = forms.EmailField(
        label="Email Address",
        help_text="Enter your business or contact email address. We will use this to follow up.",
        widget=forms.EmailInput(attrs={'placeholder': 'Your Email Address'})
    )
    subject = forms.ChoiceField(
        label="Reason for Contact",
        help_text="Select the type of inquiry.",
        choices=SUBJECT_CHOICES,
        widget=forms.Select(attrs={'type': 'select'})
    )
    message = forms.CharField(
        label="Message",
        help_text="Please provide details about the opportunity, project, or your inquiry. Feel free to include any relevant information or questions.",
        widget=forms.Textarea(attrs={'placeholder': 'Your Message'})
    )
    captcha = ReCaptchaField(
        widget=ReCaptchaV2Checkbox,
        help_text="Prove you're not a robot."
    )

    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'subject', 'message')
