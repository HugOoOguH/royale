from django.db import models
from django.conf import settings


# Create your models here.
# 
class Rarityy(models.Model):
	rarity = models.CharField(max_length = 20)
	description = models.TextField()

	def __str__(self):
		return self.rarity

class Card(models.Model):
	rarity_card = models.ForeignKey(Rarityy, related_name="rarity_cards")
	name = models.CharField(max_length = 60)
	type = models.CharField(max_length = 60)
	description = models.TextField()
	arena = models.IntegerField()
	elixir_cost = models.IntegerField()
	image = models.ImageField(upload_to = "royale", blank=True, null=True)

	def __str__(self):
		return self.name