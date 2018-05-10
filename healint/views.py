from django.http import HttpResponseNotFound,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

def main(request):    
    return render(request, '/media/disk1/Jai/jai/Downloads/jai/healint/index.html')

# def main(request):
# 	#html = "<html><body>Hi my Friend</body></html>"
# 	#return HttpResponse(html)
# 	return HttpResponseNotFound('<h1>Page not found.. Please use the healint android app</h1>')