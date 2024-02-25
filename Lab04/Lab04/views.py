from django.shortcuts import render
from django.http import HttpResponse
tax_rate=0.15
def index(request):
    return HttpResponse("This is a site to calculate tax")
def anyNumber(request):
    x =float(input("enter a number: "))
    y = x *(1+tax_rate)
    return render(request,'number.html', {'num': y })
def taxrate(request):
    return render(request,'taxes.html',{
        'tax': '15%'})
