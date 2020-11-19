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

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        str1 = ""
        str2 = params['analyzed_text']
        for char in str2:
            if char not in punctuations:
                str1 = str1 + char
        params['purpose'] = '|Removed Punctuations|'
        params['analyzed_text'] = str1

    if fullcaps == "on":
        params['analyzed_text'] = params['analyzed_text'].upper()
        params['analyzed_text'] = params['analyzed_text'].upper()
        params['purpose'] = params['purpose'] + ' |changed to uppercase|'

    if newlineremover == "on":
        str1 = ''
        str2 = params['analyzed_text']
        for char in str2:
            if char != "\n" and char != "\r":
                str1 = str1 + char
        params['analyzed_text'] = str1
        params['purpose'] = params['purpose'] + ' |Removed NewLines|'

    if extraspaceremover == "on":
        str1 = ''
        str2 = params['analyzed_text']
        for indexs, char in enumerate(str2):
            if not (str2[indexs] == " " and str2[indexs + 1] == " "):
                str1 = str1 + char
        params['analyzed_text'] = str1
        params['purpose'] = params['purpose'] + ' |Removed Extra Spaces|'

    if charcount == "on":
        str2 = params['analyzed_text']
        str1 = ('\n\nCharacter count of paragraph is ' + str(len(str2)))
        params['purpose'] = params['purpose'] + ' |Counted Characters|'
        params['analyzed_text'] = params['analyzed_text'] + str1

    if removepunc == 'off' and fullcaps == 'off' and newlineremover == 'off' and extraspaceremover == 'off' and charcount == 'off':
        return HttpResponse('Error')

    else:
        return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'about.html')
#         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
#         analyzed = ""
#         for char in djtext:
#             if char not in punctuations:
#                 analyzed = analyzed + char

#         params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
#         djtext = analyzed

#     if(fullcaps=="on"):
#         analyzed = djtext.upper()
# #         for char in djtext:
# #             analyzed = analyzed + char.upper()

#         params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
#         djtext = analyzed

#     if(extraspaceremover=="on"):
#         analyzed = ""
#         for index, char in enumerate(djtext):
#             # It is for if a extraspace is in the last of the string
#             if char == djtext[-1]:
#                     if not(djtext[index] == " "):
#                         analyzed = analyzed + char

#             elif not(djtext[index] == " " and djtext[index+1]==" "):                        
#                 analyzed = analyzed + char

#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#         djtext = analyzed

#     if (newlineremover == "on"):
#         analyzed = ""
#         for char in djtext:
#             if char != "\n" and char!="\r":
#                 analyzed = analyzed + char

#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    
#     if (numberremover == "on"):
#         analyzed = ""
#         numbers = '0123456789'

#         for char in djtext:
#             if char not in numbers:
#                 analyzed = analyzed + char
        
#         params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
#         djtext = analyzed

    
#     if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and numberremover != "on"):
#         return HttpResponse("please select any operation and try again")

#     return render(request, 'analyze.html', params)

# def about(request):
#     return render(request, 'about.html')
#     
