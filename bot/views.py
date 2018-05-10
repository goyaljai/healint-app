from django.core import serializers
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.http import HttpResponse
from bot.btpbot import *
import random
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
#import sys
from django.core.mail import EmailMessage
from bot.models import Disease
#reload(sys)
#sys.setdefaultencoding("utf-8")

import re
def isValidEmail(email):
 if len(email) > 7:
 	if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) != None:
 		return True
 return False


class LearnAPI(APIView):
	@csrf_exempt
	def get(self,request):

		#disease = request.data.get('disease', False)
		try:
			email = request.GET['email']
			print(email)
			username = User.objects.fiter(email=email)[0]
			return HttpResponse("Thanks for making our bot learn")
		except :

			return HttpResponse("""<html>
<head>
    <title>Search</title>
</head>
<body>

    <form action='/bot/learn/' method='get'>

        <input type="text" placeholder="Please Enter Email Address" name="email">
        <input type="text" placeholder = "Please Enter Your Disease" name="disease">
        <input type="submit" value="submit">
    </form>
</body>
</html>""");



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
			re_init()
			request.session['sessionKey'] = uid

			ret = {'msg': 'LoginSuccessful'}
			return Response(ret)
		else:
			u = User.objects.get(username=uid)
			u.delete()
			user = User()
			user.username = uid
			user.last_name = "0" # count for Hello
			user.set_password("healint")
			user.save()
			dis = Disease()
			dis.user = user
			dis.count = 0
			dis.save()
			re_init()
			request.session['sessionKey'] = uid
			ret = {'msg': 'LoginSuccessful'}
			return Response(ret)
			#return Response(ret)


class Logout(APIView):
	def get(self,request):
		ret = {'msg':'contact Jai Goyal if you are here'}
		return Response(ret)

	def post(self,request):
		uid = request.data.get('UniqueId', False)
		u = User.objects.get(username = uid)
		u.delete()
		re_init()
		ret = {'msg' : 'LogoutSuccessful'}
		return Response(ret)


class BotAPI(APIView):
	def get(self,request):
		ret = {'msg':'contact Jai Goyal if you are here'}
		return Response(ret)

	def post(self,request):
		#print(request.session['sessionKey'])
		uid = request.data.get('UniqueId', False)
		UserMsg = request.data.get('UserMsg', False)
		severity = request.data.get('severity',False)

		try:
			user = User.objects.get(last_name="0",username=uid)
			if(isValidEmail(UserMsg)):

				User.objects.filter(last_name="0",username=uid).update(last_name="1")
				User.objects.filter(last_name="1",username=uid).update(email=UserMsg)
				User.objects.filter(last_name="1",username=uid).update(first_name="Healint")


				#User.objects.filter(last_name="1",username=uid).update(email=UserMsg)
				ret = {'KeyboardReq':'1','BotMsg':"How Are You?",'BotSuggestion':list()}
				return Response(ret)
			else:
				ret = {'KeyboardReq':'1','BotMsg':"Please Enter Valid Email Address to chat with us !!",'BotSuggestion':list()}
				return Response(ret)


		except User.DoesNotExist:

			try:
				user = User.objects.get(last_name="1",username=uid)

				User.objects.filter(last_name="1",username=uid).update(last_name="2")
				temp=User.objects.filter(last_name="2",username=uid)
				val = str(temp.values_list("first_name",flat=True)[0])
				val+=","+UserMsg
				User.objects.filter(last_name="2",username=uid).update(first_name=val)
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
						mainSet = get_symptoms(UserMsg,uid,int(severity))

						rand_list = ["Gotcha!! Thanks, Select one more to narrow down my search. Please choose accuratly","Ohh!! This symptom helped me a lot. Diagnosing your disease...","Okay!! Please Select The Symptoms from the Given List!!","Hmmm!! Getting very close to the answer. Can you select some more symptoms for me.","Gotcha!! Thanks, Select one more to narrow down my search. Please choose accuratly","Ohh!! This symptom helped me a lot. Diagnosing your disease...","Thanks!! Getting very close to the answer. Can you select some more symptoms for me.","Gotcha!! Thanks, Select one more to narrow down my search. Please choose accuratly"]
						index = random.randint(0,len(rand_list)-1)
						botmsg = rand_list[index]

						if(len(mainSet)==9):
							botmsg = "I think you are not clear about your symptoms!! To get me started please select something from the given list"
						ret = {'isDisease':0,'KeyboardReq':'0','BotMsg':botmsg,'BotSuggestion':list(mainSet)}
						return Response(ret)
					else:
						mainSet = set()
						get_symptoms(UserMsg,uid,int(severity))
						mainSet = get_diseases()
						aa = "Thanks for using our Bot!!"
						ret = {'isDisease':1,'KeyboardReq':'1','BotMsg':aa,'BotSuggestion':list(),'DiseaseSuggestion':list(mainSet)}

						u = User.objects.get(username = uid)
						print(u.email)
						mailString = "We have predicted that you may have \n\n" + '\n'.join(str(e) for e in mainSet) + "\n\n" + "If you didnt had any of these 6 diseases, Please tell us which disease you had here \n\n " + "https://bit.ly/2K0J1J9" + "\n"
						try:

							email = EmailMessage('Diseases Suggestion After Chatting With Healint', mailString, to=[u.email])

							email.send()
						except Exception as e:
							print("email-error")
							print(e)
							pass

						u.delete()
						re_init()

						return Response(ret)

				except User.DoesNotExist:
					##print("opopopopo")
					#mainSet = get_diseases()
					user = User()
					user.username = uid
					user.last_name = "0" # count for Hello
					user.set_password("healint")
					user.save()
					dis = Disease()
					dis.user = user
					dis.count = 0
					dis.save()
					re_init()
					request.session['sessionKey'] = uid
					aa = "Error!! Out Bot is sleeping Right Now..."
					ret = {'isDisease':1,'KeyboardReq':'1','BotMsg':aa,'BotSuggestion':list(),'DiseaseSuggestion':list({"disease":"Bot is Sleeping...","url":"Wake him up by restarting the app :)"})}

					return Response(ret)
