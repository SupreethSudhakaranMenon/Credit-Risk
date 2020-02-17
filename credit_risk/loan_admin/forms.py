from django import forms
from .models import Feature
from .models import Configuration

class FeatureForm(forms.ModelForm):
	class Meta:
		model = Feature
		fields = '__all__'

class ConfigurationForm(forms.ModelForm):
	class Meta:
		model = Configuration
		fields = '__all__'