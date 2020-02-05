from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
from .filters import jobRegisterFilter


def index(request):

    jobRegisters = jobRegister.objects.all()
    return render(request, 'jobportal/main.html', {'jobRegisters': jobRegisters})

def get_context_data(self, **kwargs):
	context= super().get_context_data(**kwargs)
	context['filter'] = jobRegisterFilter(self.request.GET, queryset=self.get_queryset())
	return context

