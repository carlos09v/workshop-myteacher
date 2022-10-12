from rest_framework.views import APIView
from rest_framework.views import Response

# Create your views here.

class HomeApiView(APIView):
    def get(self , request, format=None):
        return Response({"nome": "Andre"})

# < Ir para o app teacher >