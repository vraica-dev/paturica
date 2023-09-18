from django.forms import ModelForm
from paturica.models import ContactMessage


class ContactMessageForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]


