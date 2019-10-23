from django.shortcuts import render
import pyspeedtest

def home(request):
	return render(request,"home.html",{})

def about(request):
	return render(request,"about.html",{})

def getPing(request):
	st = pyspeedtest.SpeedTest()
	ping= st.ping()
	ping=round(ping,3)
	{'p':ping}
	return render(request,"ping.html",{'p':ping})
def getsquare(n):
	count=0
	for i in range(n):
		count+=i**2
	return count

def getUpload(request):
	st = pyspeedtest.SpeedTest()
	upload = st.upload()
	upload = round(upload,4)
	{'u':upload}
	return render(request,"upload.html",{'u':upload})	

def getDownload(request):
	st = pyspeedtest.SpeedTest()
	download = st.download()
	download= round(download,4)
	{'d':download}
	return render(request,"download.html",{'d':download})	
