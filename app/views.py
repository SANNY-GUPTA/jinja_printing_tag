from django.shortcuts import render

def sa(request):
    d={'a':10,'name':'sanny'}
    return render(request,'sa.html',d)
