from django.shortcuts import render
from django.http import HttpResponse
from .models import CommType, CommReq

# Create your views here.
def index(request):
    active_comms_list = CommReq.objects.filter(complete=False).order_by('-date_accepted')
    context = {'active_comms_list': active_comms_list,}
    return render(request, 'commissions/index.html', context)

def tos(request):
    return HttpResponse("TOS page.")

def commission(request):
    return HttpResponse("Commission page.")

def account(request):
    return HttpResponse("Account page.")

def view_comm(request, user, user_id):
    return HttpResponse("Page for a user's commission with a user id.")