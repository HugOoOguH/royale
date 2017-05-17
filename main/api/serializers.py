from rest_framework import serializers
from ..models import Card

class CardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Card
		fields = ('id','rarity_card', 'name', 'type', 'description', 'arena', 'elixir_cost', 'image')