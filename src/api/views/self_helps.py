from rest_framework.views import APIView
from rest_framework.response import Response
import json

class SelfHelpViews(APIView):
    def get(self, response):
        version:int = 1
        with open('./_selfHelps/selfHelp.json') as file:
            map = json.loads(file.read())

            return Response({
                'version': version,
                'data': map,
            })