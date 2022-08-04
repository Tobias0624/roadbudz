from django.shortcuts import get_object_or_404, render
from .models import *

# Create your views here.

def index(request):
    return render(request, 'strainSearch/index.html')

def weedList(request):
    type_list = strains.objects.all()
    return render(request, 'strainSearch/strains.html', {'type_list':type_list})

def getWeedDescription(request, id):
    weed_descript = get_object_or_404(strains, pk=id)
    context = {
        'weed_descript': weed_descript,
    }
    return render(request, 'strainSearch/more.html', context=context)


