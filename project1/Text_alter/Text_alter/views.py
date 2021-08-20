from django.http import HttpResponse
from django.shortcuts import redirect, render

def welcome(request):
    # return HttpResponse("this is home")
    return render(request, "welcome.html")

def contact(request):
    return render(request, "contact.html")

def home(request):
    return render(request, "home.html")

def analyze(request):
    textval = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    ''' whenever u make get request so u need to wright "request.GET.get" gives u value as it is and second argument is default '''
    caps = request.POST.get('caps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremove = request.POST.get('spaceremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    binary = request.POST.get('binary', 'off')
    ''' here removepunc and all other are checkbox so if they are checked then values is "on"  otherwise value is "off" '''
    analyzed = ""
    purpose = ""
    if textval == "":
        analyzed = ""
    elif removepunc == "on":
        punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        for i in textval:
            if i not in punctuations:
                analyzed += i
        purpose = "Punctuations Removed"

    elif caps == "on":
        analyzed = textval.upper()
        purpose = "capitalized"

    elif newlineremover == "on":
        for i in textval:
            print(i, "i")
            # if i != "\n":
            if i != "\n" and i != "\r":
                analyzed += i
        purpose = "New Line Removed"

    elif spaceremove == "on":
        for count, i in enumerate(textval):
            if count != len(textval) - 1:
                if not (textval[count] == " " and textval[count + 1] == " "):
                    analyzed += i
        purpose = "Extra Space Removed"

    elif charcount == "on":
        analyzed = 0
        for i in textval:
            if i != " ":
                analyzed += 1
        purpose = "Character Count"
    
    elif binary == "on":
        try:
            analyzed = format(int(textval), "b")
        except:
            analyzed = ''.join(format(ord(i), 'b') for i in textval)
        purpose = "binary"

    params = {'purpose': f"{purpose}", 'Analyzed_text' : analyzed}
    return render(request, "analyze.html", params)