from django.shortcuts import render,render_to_response
from django.template import Context, RequestContext

def home(request):
	return render_to_response('home.html', context_instance = RequestContext(request))
