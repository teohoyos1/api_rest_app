from django.http import Http404
from rest_framework import generics, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
#django
from django.shortcuts import get_object_or_404

from api.authentication import TokenAuthentication
from .models import Product
from .serializers import ProductSerializer


#Class Based View List all, detail and Create
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def data_create(self, serializer):
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        quantity = serializer.validated_data.get('quantity')
        if description is None:
            description = title
        serializer.save(description=description)


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = 'pk'


#update Class based view Product
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def data_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.title

#delete Class based view Product
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def data_destroy(self, instance):
        super().data_destroy(instance)

#Function Based View List all, detail and Create
@api_view(['GET','POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    data = {}
    if request.method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        querySet = Product.objects.all()
        data = ProductSerializer(querySet, many=True).data
        return Response(data)


    if request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description')
            price = serializer.validated_data.get('price')
            quantity = serializer.validated_data.get('quantity')
            if description is None:
                description = title
            serializer.save(description=description)
            return Response(serializer.data)
        return Response({"invalid":"Datos incorrectos"},status=400)