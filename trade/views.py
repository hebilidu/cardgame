from .models import Card
from django.views import generic
from django.shortcuts import render

# Create your views here.
class CardListView(generic.ListView):
    model = Card
    template_name = 'listcard.html'
    context_object_name = 'cards'


class CardDetailView(generic.DetailView):
    model = Card
    template_name = 'viewcard.html'
    context_object_name = 'card'

def shuffle(request):
    """Display for for creating a deck instance: distribution of the cards among a given group of players"""
    # 1. ask for number of players
    # 2. then display formset asking to pick the players from drop-down lists
    # 3. then display the hands for that deck
    return render(request, 'listcard')