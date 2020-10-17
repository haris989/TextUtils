# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover','off')
    changefont=request.POST.get("changefont",'off')
    purpose="you  "

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        purpose=purpose+"removed punctuations "

        params = {'purpose':purpose, 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        purpose=purpose+"capitalized text"

        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                    if not(djtext[index] == " "):
                        analyzed = analyzed + char

            elif not(djtext[index] == " " and djtext[index+1]==" "):                        
                analyzed = analyzed + char
        purpose=purpose+"removed extraspaces"

        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
        purpose=purpose+"newlineremover "

        params = {'purpose': purpose, 'analyzed_text': analyzed}
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        purpose=purpose+"removed numbers"
        
        params = {'purpose': purpose, 'analyzed_text': analyzed}
        djtext = analyzed

    if (changefont=="on"):
        analyzed=djtext
        purpose=purpose+"changed font"
        params={'purpose':purpose,'analyzed_text':analyzed,'a':'24'}

    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on" and changefont!='on'):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')