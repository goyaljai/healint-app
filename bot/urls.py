from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^login/', views.Login.as_view(), name='bot-login'),
    url(r'^logout/', views.Logout.as_view(), name='bot-logout'),
    #url(r'^textDigger/', views.TextDigger.as_view(), name='bot-textDigger'),
    #url(r'^optionsDigger/', views.OptionsDigger.as_view(), name='bot-optionsDigger'),
    url(r'^chat/',views.BotAPI.as_view(),name='bot-chatter'),
   # url(r'',views.main),
]
