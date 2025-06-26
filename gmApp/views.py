from django.shortcuts import render
from .models import *
from .serializer import *
from django.core.paginator import Paginator
from rest_framework.generics import *

# Create your views here.
class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def get_products(request):
    product = Product.objects.all()
    paginator = Paginator(product, 5)  # Show 3 movies per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,  # same variable name as movie_list
    }
    return render(request, 'get_products.html', context)
