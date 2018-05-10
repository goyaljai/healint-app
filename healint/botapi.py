from django.core import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import HttpResponse

class ComplaintView(APIView):
 
    parser_classes = (MultiPartParser,FormParser,FileUploadParser,) #  not needed but still
    def get(self,request):
        result = functions.get_complaint()
        return Response(result)

    def post(self,request):
        image = request.FILES["image"]
        email = request.data.get('email', False)
        title = request.data.get('title', False)
        description = request.data.get('description', False)
        latitude = request.data.get('latitude', False)
        longitude = request.data.get('longitude', False)
        status = request.data.get('status', False)

        file = open("kmeansData","a")
        file.write(str(latitude) + " " + str(longitude) + "\n")
        file.close()
        result = functions.complaint(email, title, description,latitude,longitude,status,image)
        return Response(result)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

