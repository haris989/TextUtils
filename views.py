#created by me
from django.http import HttpResponse
from django.shortcuts import render
from fpdf import FPDF
import string,random
def home(request):
    
    return render(request,'index2.html') 

def about(request):
    return render(request,"aboutus.html")


def analyze(request):
    #get text
    gettext=request.GET.get('text','default') #get text from text area
    removepunc=request.GET.get('removepunch','off') #get check box value
    newlineremove=request.GET.get('newlineremover','off')
    fullcaps=request.GET.get('fullcaps','off')
    charcount=request.GET.get('charcount','off')
    createpdf=request.GET.get('pdf','off')
    textfile=request.GET.get('textfile','off')
   
    
    if removepunc =="on":

        punctutions='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in gettext:
            if char not in punctutions:
                analyzed=analyzed+char

        #analyze text
        param={'purpose':'Remove punctuations','analyzed_text':analyzed}
        return render(request,"analyze2.html",param)

    elif(fullcaps=='on'):
        analyzed=""
        for char in gettext:
            analyzed=analyzed+char.upper()

        param={'purpose':'covert to upper case','analyzed_text':analyzed}
        return render(request,"analyze2.html",param)
        
    elif(newlineremove=='on'):
        analyzed = ""
        for char in gettext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char


        param={'purpose':'covert to upper case','analyzed_text':analyzed}
        return render(request,"analyze2.html",param)

    elif(charcount=='on'):
        
        cw=0
        for char in gettext:
            words=char.split()
            cw+=len(words)
    
        analyzed=cw
        param={'purpose':'count characters','analyzed_text':analyzed}
        return render(request,"analyze2.html",param)
        
    
    elif(createpdf=='on'):
        
        
        res = ''.join(random.choices(string.ascii_uppercase,k=5)) 
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("Arial",size=15)
        
        
        a=gettext[:80]+"\n"
        b=gettext[80:160]+"\n"
        c=gettext[160:320]+"\n"
        d=gettext[320:]+"\n"
  
        pdf.cell(200, 10, txt = a, ln = 1) 
        pdf.cell(200, 10, txt = b, ln = 1) 
        pdf.cell(200, 10, txt = c, ln = 1)
        pdf.cell(200, 10, txt = d, ln = 1) 

        
        
        pdf.output("%s.pdf"%res)
        analyzed="pdf is created in your computer with name %s"%(res)
        param={'purpose':'created pdf','analyzed_text':analyzed}
        return render(request,"analyze2.html",param)
        
        
        
    
    elif(textfile=='on'):
        
        
        res = ''.join(random.choices(string.ascii_uppercase,k=5)) 
        
        f=open(res,'w')
        f.write(gettext)
        f.close()
        
        analyzed="text file  is created in your computer with name %s"%(res)
        param={'purpose':'created pdf','analyzed_text':analyzed}
        return render(request,"analyze2.html",param)
        
    else:
        return HttpResponse("ERROR SELECT ATLEAST ONE OPTION")
    



    