from django.shortcuts import render
import requests
import sys
from subprocess import run,PIPE
from Insertion.models import Ticket_Table,Notes_Table
import uuid 
from copy import deepcopy

def index(request):

    return render(request,'index.html')

def insert(request):
    
    ph= request.POST.get('ph')
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    cit=request.POST.get('city')
    add=request.POST.get('add')
    itype=request.POST.get('itype')
    I_dscr_no=request.POST.get('datas')
    Tkt_no=uuid.uuid4().hex[:6].upper()
    index_notes=request.POST.get('index_notes')
    Tkt_status="Open"
    tickets_info=Ticket_Table(ph_no=ph,firstname=fname,lastname=lname,city=cit,address=add,Issuetype=itype,
    Issue_Desc=I_dscr_no,Ticket_no=Tkt_no,Ticket_status=Tkt_status)
    tickets_info.save()
    notes_info=Notes_Table(Ticket_no=Tkt_no,Ticket_notes=index_notes)
    notes_info.save() 
    return render(request,'Info.html',{'ph':ph,'fname':fname,'lname':lname,'city':cit,'address':add,
                'itype':itype,'idscr':I_dscr_no,'tkt_no':Tkt_no,'index_notes':index_notes,'t_status':Tkt_status})

def display(request):

    alldata= Ticket_Table.objects.all()
    context= {'alldata': alldata}
    return render(request,"display.html",context)

def notes(request):
    note=request.GET.get('note')
    information=Ticket_Table.objects.filter(Ticket_no=note)
    query = Notes_Table.objects.filter(Ticket_no=note)
    Submit_notes=request.GET.get('notes')
    Update_status=request.GET.get('t_status')
    if(Submit_notes!=None):
        note_info=Notes_Table(Ticket_no=request.GET.get('note'),Ticket_notes=Submit_notes)
        note_info.save()
        query = Notes_Table.objects.filter(Ticket_no=note)
    if(Update_status!=None):
        Update = Ticket_Table.objects.get(Ticket_no=note)
        Update.Ticket_status=Update_status
        Update.save()
    return render(request,'notes.html',{'Ticket_no':note,'context_note':query,'alldata': information})


