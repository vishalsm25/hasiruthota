from django.shortcuts import render
from .models import featured_product
from .models import new_product, best_plants

# Create your views here.
def index(request):
    fps = featured_product.objects.all()
    nps = new_product.objects.all()
    bps = best_plants.objects.all()
    return render(request, 'index.html', {'fps': fps , 'nps': nps, 'bps': bps})


