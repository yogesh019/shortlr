from django.shortcuts import render,get_object_or_404
import random,string,json
from .models import Urls
from django.http import HttpResponseRedirect,HttpResponse
from django.conf import settings
from django.core.context_processors import csrf

# Create your views here.

def index(request):
    context={}
    context.update(csrf(request))
    return render(request,'shortenersite/index.html',context)

def redirect_original(request,short_id):
    url=get_object_or_404(Urls,pk=short_id) # get object , if not found return 404 error
    url.count+=1
    url.save()
    return HttpResponseRedirect(http.httpurl)
    

def shorten_url(request):
    url=request.POST.get("url",'')
    if not (url==''):
        short_id=get_short_code()
        b=Urls(httpurl=url,short_id=short_id)
        b.save()
        response_data={}
        response_data['url']=settings.SITE_URL+"/"+short_id
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    return HttpResponse(json.dumps({"error":"error-occurs"},content_type="application/json")


def get_short_code():
    length=6
    char=string.ascii_uppercase+string.digits+string.ascii_lowercase
    # if the randomly generate short_id is used than generate next
    while True:
        short_id=''.join(rando.choice(char) for x in range(length))
        try:
            temp=Urls.objects.get(pk=short_id)
        except:
            return short_id

