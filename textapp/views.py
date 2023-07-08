from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def analyze(request):
    if request.method=="GET":
        text=request.GET.get('text')

        punc = """!"#$%&'()*+,-./\:;<=>?@[]^_`{|}~"""

        analyzed = ""
        for char in text:
            if char not in punc:
                analyzed=analyzed+char

        aresult={
            'text':analyzed
        }

        

    return render(request,"result.html",aresult)