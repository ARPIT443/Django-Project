from django.http import HttpResponse
from django.shortcuts import render

def index1(request):
    return render(request,'index1.html')


def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    capitalize = request.POST.get('capitalize', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed= analyzed+char
        djtext = analyzed

    if capitalize == "on":
        analyzed=""
        analyzed = djtext.upper()
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and  char!= '\r':
                analyzed = analyzed + char
        djtext = analyzed

    if extraspaceremover == "on":
        import re
        analyzed = re.sub(' +', ' ', djtext)

    if (removepunc!= 'on' and capitalize!= 'on' and newlineremover != 'on' and extraspaceremover!= 'on'):
        return HttpResponse("<h1>Please Choose an Operation to perform </h1>")


    params = {'purpose': 'Remove Extra Space', 'analyzed_text': analyzed}
    return render(request, 'analyse.html', params)







