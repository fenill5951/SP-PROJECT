from django.shortcuts import render,redirect
from django.contrib import messages 
from django.http import HttpResponse , HttpResponseRedirect
import sqlite3
connection=sqlite3.connect('dbonlinebanking.sql')
c=connection.cursor()
c.execute('CREATE TABLE IF NOT EXISTS tblregistration(RedID INTEGER PRIMARY KEY AUTOINCREMENT ,Firstname TEXT , Lastname TEXT , username TEXT , Password TEXT , EmailID TEXT,Account No TEXT ,Balance Real ,Address TEXT )')
# Create your views here.
def login_view(request):
	if request.method=='POST':
		username=request.POST['txtusername']
		password=request.POST['txtpassword']
		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('SELECT RedID ,Account No,Balance from tblregistration WHERE username="%s" AND Password="%s" ' %(username,password))
		records=c.fetchall()
		if records is not None :
			for a, b, c in records:
				request.session['RedID']=a
				request.session['Account No']=b
				request.session['Balance']=c
				return render(request,'onlinebankingapp/Home.html')
		else :
			return render(request,'onlinebankingapp/dummy1.html')
		connection.commit()
		connection.close()
		return redirect('/dummy1/')

	elif request.method=='GET':
		return render(request,'onlinebankingapp/login.html')



def registration_view(request):
	if request.method=='POST':
		firstname=request.POST['txtfirstname']
		lastname=request.POST['txtlastname']
		username=request.POST['txtusername']
		password=request.POST['txtpassword']
		emailid=request.POST['txtemailid']
		accountno=request.POST['txtaccountno']
		balance=request.POST['txtbalance']
		address=request.POST['txtaddress']
		mobileno=request.POST['txtmobileno']

		connection=sqlite3.connect('dbonlinebanking.sql')
		c=connection.cursor()
		c.execute('INSERT INTO tblregistration values(Null,?,?,?,?,?,?,?,?)',(firstname,lastname,username,password,emailid,accountno,balance,address))
		connection.commit()
		connection.close()
		return render(request,'onlinebankingapp/display.html')
	elif request.method=='GET':
		return render(request,'onlinebankingapp/registration.html')





def home_view(request):
	return render(request,'onlinebankingapp/Home.html')



		