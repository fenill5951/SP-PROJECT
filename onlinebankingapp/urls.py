from django.urls import path
from onlinebankingapp import views

urlpatterns=[
	path('login/',views.login_view),
	path('registration/',views.registration_view),
	path('',views.home_view),
	
]