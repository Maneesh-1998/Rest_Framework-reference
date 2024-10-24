from rest_framework.response import Response
from rest_framework.views  import APIView
from . models import *
from . serializers import *
# Create your views here.
class ProductsView(APIView):
    def get(self,request):
        all_products=products_2.objects.all()
        serialized_products=products_serializers(all_products,many=True).data
        return Response(serialized_products)
class ProductsViewById(APIView):
    def get(self,request,id):
        product=products_2.objects.get(id=id)
        single_product=products_serializers(product).data
        return Response(single_product)