from email import header
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.serializers import ProductSerializer
from product.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):

    """
    DRF API View
    """

    instance = Product.objects.all().order_by("?").first()

    data = {}
    if instance:
        #data = model_to_dict(instance)
        data = ProductSerializer(instance).data
    return Response(data)


@api_view(["POST"])
def api_post_home(request, *args, **kwargs):
    """
    DRF API View
    """
    data = request.data
    serializer = ProductSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        data = serializer.data
        return Response(data)
    return Response({"invalid":"Datos incorrectos"},status=400)

def read_body(request):

    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    #return JsonResponse(data, headers={"content_type":"application/json"})
    return JsonResponse(data)