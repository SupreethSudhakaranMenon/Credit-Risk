from django.db import models

# Create your models here.
class Feature(models.Model):
	VALUE_CHOICES = [
		('Bi', 'Binary'),
		('No', 'Nominal'),
		('In', 'Interval'),
		('Ra', 'Ratio'),
	]
	DATA_CHOICES = [
		('Nu', 'Numeric'),
		('Ch', 'Character'),
		('Da', 'Date'),
	]
	CATEGORY_CHOICES = [
		('In', 'Individual'),
		('Co', 'Company'),
		('Cy', 'Country'),
	]
	name = models.CharField(max_length=200, primary_key=True)
	value = models.CharField(max_length=10, choices=VALUE_CHOICES)
	data_type = models.CharField(max_length=10, choices=DATA_CHOICES)
	category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

	def __str__(self):
		return self.name

# Configuration Model
class Configuration(models.Model):
	PRODUCT_CHOICES = [
		('Ag', 'Agriculture'),
		('Pe', 'Personal'),
		('Ca', 'Capital'),
		('Ra', 'Ratio'),
	]
	CATEGORY_CHOICES = [
		('In', 'Individual'),
		('Or', 'Organisation'),
		('Co', 'Country'),
		('Cr', 'CreditHistory'),
		('Lo', 'Loan'),
	]
	CHARACTERISTIC_CHOICES = [
		('Ag', 'Age'),
		('In', 'Income'),
		('Ge', 'Gender'),
	]

	COLOUR_CHOICES = [
		('Gr', 'Green'),
		('Am', 'Amber'),
		('Re', 'Red'),
	]
	product = models.CharField(max_length=20, choices=PRODUCT_CHOICES)
	category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
	characteristic = models.CharField(max_length=20, choices=CHARACTERISTIC_CHOICES)
	colour = models.CharField(max_length=20, choices=COLOUR_CHOICES)