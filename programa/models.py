from django.db import models

class Item (models.Model): 
	nome = models.CharField(max_length='100',
		blank=False,
		null=False)
	valor = models.DecimalField(max_digits=13, decimal_places=2, default=0)

	