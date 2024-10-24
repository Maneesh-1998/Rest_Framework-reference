from rest_framework.response import Response
from rest_framework.views  import APIView
from . models import *
# Create your views here.

class ProductsView(APIView):

    def get(self,request):
        all_products=products.objects.all()
        products_data=[]
        for product in all_products:
            single_product={
                "id":product.id,
                "product_name":product.product_name,
                "code":product.code,
                "price":product.price,
                #"category_reference_id":product.category_reference_id //foreign key
                }
            products_data.append(single_product)
        return Response(products_data)

    def post(self,request):
        new_product=products(product_name=request.data["product_name"],code=request.data["code"],price=request.data["price"])
        """new_product=products(product_name=request.data["product_name"],code=request.data["code"],
        price=request.data["price"],category_reference_id=request.data['category_reference_id']) """
        new_product.save()
        return Response("data saved")


class ProductsViewById(APIView):
    def get(self,request,id):
        product=products.objects.get(id=id)
        single_product={
                "id":product.id,
                "product_name":product.product_name,
                "code":product.code,
                "price":product.price,
                #"category_reference_id":product.category_reference_id //foreign key concept
                }
        return Response(single_product)
    
    def patch(self,request,id):
        product=products.objects.filter(id=id)
        product.update(product_name=request.data["product_name"],code=request.data["code"],price=request.data["price"])
        """new_product=products(product_name=request.data["product_name"],code=request.data["code"],
        price=request.data["price"],category_reference_id=request.data['category_reference_id']) """
        return Response("update")
    
    def delete(self,request,id):
        product=products.objects.get(id=id)
        product.delete()
        return Response("deleted")


class CategoryViewById(APIView):
    def delete(self,request,id):
        category=Category.objects.all(id=id)
        category.delete()
        return Response("Deleted")