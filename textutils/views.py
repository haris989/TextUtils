# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render
from googletrans import Translator
translator = Translator()

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
    transtext = request.POST.get('transtext', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
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

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        
    if transtext == "on":
        translations = translator.translate(djtext, dest='hi')
        analyzed = translations.text
        params = {'purpose': 'Your Translated Text', 'analyzed_text': analyzed}
       
    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on"):
        return HttpResponse("please select any operation and try again")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')
