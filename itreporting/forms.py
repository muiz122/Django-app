from django import forms
from .models import Registration, Module, Course

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['course']  # Only select the course during registration

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limit courses in the form to available ones
        self.fields['course'].queryset = Course.objects.all()
        self.fields['course'].label = "Select Course"
