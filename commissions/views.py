from django.shortcuts import get_object_or_404, render
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
    active_commtypes_list = CommType.objects.filter(active=True).order_by('price')
    context = {'active_commtypes_list': active_commtypes_list,}
    return render(request, 'commissions/commission.html', context)

def account(request):
    return HttpResponse("Account page.")

def view_comm(request, id):
    commreq = get_object_or_404(CommReq, pk=id)
    return render(request, 'commissions/commreq.html', {'commreq': commreq,})