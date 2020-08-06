from django.shortcuts import render
from api import result

# Create your views here.



def index(request):
	try:
		if request.method=='POST':
			data=request.POST.copy()
			n=int(data.get('number'))
			res=result(n)
			data={'number':n,'result':res}

			return render(request,'chat/result.html',data)

		return render(request,'chat/index.html')
	except:
		return render(request,'chat/index.html')
def blog(request):
	return