
from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
import json

def index(requset):
  return render(requset, 'index.html')
  
    #return HttpResponse(" this is HOME page.")



def first(requset):
   
   return render(requset, 'first.html')   

def jorhat(requset):
   
   return render(requset, 'jorhat.html')    
def manikar(requset):
   
   return render(requset, 'manikar.html')  

def kasol(requset):
   
   return render(requset, 'kasol.html') 
   

def about(requset):
   
   return render(requset, 'about.html')
   
    

def acadmics(requset):
   return render(requset, 'destination.html')
     

    # return HttpResponse(" this is your service😉page.")

def contact(requset):
    if requset.method == "POST":
        name = requset.POST.get('name') 
        email = requset.POST.get('email')
        reason = requset.POST.get('reason')
        contact = Contact(name=name, email=email, reason=reason, date=datetime.today())
        contact.save()
        messages.success(requset, "This is recorded just take care of yourself killer is on the way😈")
      
    return render(requset, 'contact.html')


 