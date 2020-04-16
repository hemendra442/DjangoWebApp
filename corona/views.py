from django.shortcuts import render
from .models import Destination

# Create your views here.
def home(request):
    return render(request,'home.html')

def index(request):
    dest1 = Destination()
    dest2 = Destination()
    dest3 = Destination()

    dest1.id = 1
    dest1.price=1000
    dest1.title="Hyderabad"
    dest1.subtitle="Historic Place for AndhraPradesh"
    dest1.img = 'destination_1.jpg'
    dest2.id = 2
    dest2.price=2000
    dest2.title="Bangalore"
    dest2.subtitle="Historic Place for Karnataka"
    dest2.img = 'destination_2.jpg'

    dest3.id = 3
    dest3.price=500
    dest3.title="Chennai"
    dest3.subtitle="Historic Place for Tamilanadu"
    dest3.img = 'destination_3.jpg'

    dests = [dest1, dest2, dest3]

    return render(request,'myindex.html', {'dests':dests})