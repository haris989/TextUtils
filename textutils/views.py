# This is harry bhai ka code
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
    CharType = request.POST.get('CharType','off')
    SenType = request.POST.get('SenType','off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!|()-[]{};:'"\,<>./?@#$%^&*_~'''
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
        djtext = analyzed
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

# Below this is my code
    if(CharType=="on"):
        djtext = djtext
        analyzed = ""
        capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        small = 'abcdefghijklmnopqrstuvwxyz'
        symbol = '''!()-[]|{};:'"\,<>./?@#$%^&*_~'''
        capitalcount = 0
        smallcount = 0
        symbolcount = 0
        blankcount = 0
        for char in djtext:
            if char in capital:
                capitalcount +=1
            if char in small:
                smallcount +=1
            if char in symbol:
                symbolcount +=1
            if char == ' ':
                blankcount += 1
        
        analyzed = f"The give text contains {capitalcount}  capital letters.\nThe give text contains {smallcount} small letters.\nThe give text contains {symbolcount} symbol.\nThe give text contains {blankcount} blanks.\n"
        params = {'purpose': 'Character Type counter', 'analyzed_text': analyzed}
        djtext = analyzed
    
    if SenType == "on":
        analyzed = ""
        asserativecount = 0
        exclamatorycount = 0
        questioncount = 0
        for char in djtext:
            if char == '.':
                asserativecount +=1
            if char == '!':
                exclamatorycount +=1
            if char == '?':
                questioncount +=1

        analyzed = f"The given text contains {asserativecount} asserative sentences.\nThe given text contains {exclamatorycount} exclamatory sentences.\nThe given text contains {questioncount} interrorgative sentences.\n"
        params = {'purpose': 'Sentence Type Counter', 'analyzed_text': analyzed}
        djtext = analyzed
    
# to this is mine code

    
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on" and CharType!='on' and SenType!='on'):
        return HttpResponse('please select any operation and try again')

    

    

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')