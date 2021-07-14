# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


ef analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'Nothing Enterrred')
    djtext_list = list(djtext)
    del djtext

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    # creating needs
    params = {'purpose': '', 'analyzed_text': ""}
    punctuations = list('''!()-[]{};:'"\,<>./?@#$%^&*_~''')
    removal_list = []

    # main for loop
    for index in range(len(djtext_list)):
        char = djtext_list[index]
        removal = False

        if removepunc == "on":
            if djtext_list[index] in punctuations:
                removal = True
            if index == 0:
                params['purpose'] = params['purpose'] + \
                    ", Removed Punctuations"

        if fullcaps == "on":

            djtext_list[index] = djtext_list[index].upper()
            if index == 0:
                params['purpose'] = params['purpose'] + ", Capitalised Text"

        if(extraspaceremover == "on"):
            if index + 2 < len(djtext_list):
                if (djtext_list[index] == " " and djtext_list[index+1] == " "):
                    removal = True
                if index == 0:
                    params['purpose'] = params['purpose'] + \
                        ", Unneeded spaces removed"

        if (newlineremover == "on"):

            if djtext_list[index] == "\n" and djtext_list[index + 1] == "\n":
                removal = True
            if index == 0:
                params['purpose'] = params['purpose'] + ", New lines removed"

        if removal:
            removal_list.append(char)

    djtext_list = [e for e in djtext_list if e not in removal_list]

    params['analyzed_text'] = "".join(djtext_list)
    params['purpose'] = params['purpose'].lstrip(",")

    return render(request, 'analyze.html', params)

def about(request):
    return render(request, 'about.html')
