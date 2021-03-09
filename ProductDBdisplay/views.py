from ProductDBdisplay.serializers import Serializationclass
from ProductDBdisplay.models import Productmodel
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def ShowProduct(request):
    if request.method == 'GET':
        results = Productmodel.objects.all()
        serialize = Serializationclass(results, many = True)
        return Response(serialize.data)