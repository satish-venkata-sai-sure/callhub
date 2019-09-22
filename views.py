from django.shortcuts import render
from django.http import HttpResponse
import  time
# Create your views here.

def home(request):
	return render(request,'home.html',{'name':'kiran'})

def fibapp(request):
	start=time.time()
	cd=request.GET['num1']
	if(cd is not None and type(cd)==str):
		n=int(cd)
	else:
		return render(request,'final.html',{'fibo':'Enter valid Number','tme':'---'})
	n=int(cd)
	a=0
	b=1
	l=[]
	for i in range(n+1):
		l.append(a)
		c=a+b
		a=b
		b=c
		lst=l[-1]
		end=time.time()
		tltme=float(end-start)
	return render(request,"final.html",{'fibo':lst,'tme':tltme})
