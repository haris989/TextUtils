from django.shortcuts import render
from Contact.models import Contact
from datetime import datetime

# Create your views here.
def contact(request):
	if(request.method== "POST"):
		name=request.POST.get("name")
		mail=request.POST.get("email")
		reason=request.POST.get("reason")
		contact=Contact(name=name,email=mail,desc=reason,date=datetime.now())
		contact.save()
		alert={"alert":'''Your Request has been Submited'''}
		return render(request, 'contact.html',alert)
	else:
		return render(request, 'contact.html')
    
    