from django.shortcuts import render
import pyspeedtest

def home(request):
	st = pyspeedtest.SpeedTest()
	ping= st.ping()
	download = st.download()
	upload = st.upload()
	{'p':ping,'d':download,'u':upload}
	return render(request,"home.html",{'p':ping,'d':download,'u':upload})

def about(request):
	return render(request,"about.html",{})