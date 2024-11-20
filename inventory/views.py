from django.shortcuts import render
from django.http import HttpResponse

from .models import Drinks_Inventory
def index(response):
    return HttpResponse('inventory for drinks')

def Inventory_list(request):
    inventory = Drinks_Inventory.objects.all()
    context = {'inventory' : inventory}
    return render(request, 'inventory/Inventory_list.html' , context = context )