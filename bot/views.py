from django.core import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import HttpResponse
from btpbot import *
from django.contrib.auth.models import User
import sys
from bot.models import Disease
reload(sys)
sys.setdefaultencoding("utf-8")

class Login(APIView):
	def get(self,request):
		ret = {'msg':"contact Jai Goyal if you are here"}
		return Response(ret)

	def post(self,request):

		uid = request.data.get('UniqueId', False)
		try:
			username = User.objects.get(username=uid)
		except User.DoesNotExist:
			username = None

		if username is None:
			user = User()
			user.username = uid
			user.last_name = "0" # count for Hello
			user.set_password("healint")
			user.save()
			dis = Disease()
			dis.user = user
			dis.count = 0
			dis.save()

			ret = {'msg': 'LoginSuccessful'}
			return Response(ret)
		else:
			ret = {'msg': 'contact Jai Goyal if you are here'}
			return Response(ret)


class Logout(APIView):
	def get(self,request):
		ret = {'msg':'contact Jai Goyal if you are here'}
		return Response(ret)

	def post(self,request):
		uid = request.data.get('UniqueId', False)
		u = User.objects.get(username = uid)
		u.delete()
		ret = {'msg' : 'LogoutSuccessful'}
		return Response(ret)


class BotAPI(APIView):
	def get(self,request):
		ret = {'msg':'contact Jai Goyal if you are here'}
		return Response(ret)

	def post(self,request):

		uid = request.data.get('UniqueId', False)
		UserMsg = request.data.get('UserMsg', False)

		try:
			user = User.objects.get(last_name="0",username=uid)
			User.objects.filter(last_name="0",username=uid).update(last_name="1")
			User.objects.filter(last_name="1",username=uid).update(first_name=UserMsg)
			ret = {'KeyboardReq':'1','BotMsg':"'How Are You? '' '",'BotSuggestion':list()}
			return Response(ret)

		except User.DoesNotExist:

			try:
				user = User.objects.get(last_name="1",username=uid)

				User.objects.filter(last_name="1",username=uid).update(last_name="2")

				st = init(UserMsg) + " Please Tell Me Your Symptom?"
				global vvv
				ret = {'KeyboardReq':'1','BotMsg':st,'BotSuggestion':list()}
				return Response(ret)

			except User.DoesNotExist:

				try:

					user = User.objects.get(last_name="2",username=uid)
					dis = Disease.objects.filter(user=user)
					val = dis.values_list("count",flat=True)[0]
					val += 1
					Disease.objects.filter(user=user).update(count=val)

					if(val<=5):
						mainSet = set()
						mainSet = get_symptoms(UserMsg,uid)
						ret = {'isDisease':0,'KeyboardReq':'0','BotMsg':"Ok!! Now, Please Select The Symptoms from the Given List!!' '",'BotSuggestion':list(mainSet)}
						return Response(ret)
					else:
						mainSet = set()
						get_symptoms(UserMsg,uid)
						mainSet = get_diseases()
						aa = "I have predicted that you have " + str(mainSet)
						ret = {'isDisease':1,'KeyboardReq':'1','BotMsg':'','BotSuggestion':list(),'DiseaseSuggestion':list(mainSet)}

						return Response(ret)

						u = User.objects.get(username = uid)
						u.delete()

						return Response(ret)







				except User.DoesNotExist:
					#print("opopopopo")
					ret = dict()
					return Response(ret)
