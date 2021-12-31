from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import CommType, CommReq


# Create your views here.
def index(request):
    active_comms_list = (
        CommReq.objects
        .filter(complete=False) #Still in-progress
        .filter(date_accepted__isnull=False) #Accepted
        .order_by('date_accepted'))
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

def submit(request):
    #Make a new CommReq to be saved into the database if and only if TOS was checked
    #TODO: alert me

    #if TOS checked, attempt to save CommReq into database
    if request.POST['tos']:
        #attempt to get commType
        try:
            commType = CommType.objects.get(pk=request.POST['commtype_id'])
        except (KeyError, CommType.DoesNotExist):
            return HttpResponseRedirect(reverse('commissions:commission'))
            #TODO: do something meaningful and show error

        else:
            newreq = CommReq(
                #TODO: handle buffer overflow
                commType=commType,
                date_mod=timezone.now(),
                contact=request.POST['contact'],
                file=request.POST['file'],
                charnotes=request.POST['charnotes'],
                comments=request.POST['comments'],
            ) # TODO move everything around to handle .POST errors
            newreq.save()

            #TODO make this go somewhere meaningful
            return HttpResponseRedirect(reverse('commissions:index'))

    #if TOS not checked, reload with error
    else:
        return HttpResponseRedirect(reverse('commissions:commission'))
        #TODO: do something meaningful and show error