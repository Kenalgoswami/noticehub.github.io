#from django.shortcuts import render
#from django.http import HttpResponse 
#from myadmin.models import Notice

# Create your views here.
#def all_notice(request):
 #   allnotices = Notice.objects.all()
	 #context ={}
#	context = {'result': allnotices}
      
	#return render(request,'user/notice.html')
	 #return render(request,'user/index.html',context)

from django.shortcuts import render
from myadmin.models import Notice

def all_notice(request):
    allnotices = Notice.objects.all()
    context = {'result': allnotices}
    return render(request, 'user/notice.html', context)
