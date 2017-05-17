from django.contrib import admin
from .models import Rarityy, Card
# Register your models here.
class RarityyAdmin(admin.ModelAdmin):
	list_display = ('id', 'rarity',)
	list_filter = ('rarity',)
	search_fields = ('rarity', 'description',)
	ordering = ['rarity',]

class CardAdmin(admin.ModelAdmin):
	list_display = ('name', 'type', 'arena', 'elixir_cost',)
	list_filter = ('type', 'arena', 'elixir_cost',)
	search_fields = ('name', 'description', 'type',)
	ordering = ['name',]

admin.site.register(Rarityy, RarityyAdmin)
admin.site.register(Card, CardAdmin)