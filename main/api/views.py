from ..models import Card
from .serializers import CardSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class CardList(generics.ListCreateAPIView):
	queryset = Card.objects.all()
	serializer_class = CardSerializer
	permission_classes = (AllowAny,)


