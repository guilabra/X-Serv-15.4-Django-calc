from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def suma(request, number1, number2):
    number = int(number1) + int(number2)
    return HttpResponse('El resultado de la suma es: %s'%str(number))
def resta(request, number1, number2):
    number = int(number1) - int(number2)
    return HttpResponse('El resultado de la resta es: %s'%str(number))
def multiplica(request, number1, number2):
    number = int(number1) * int(number2)
    return HttpResponse('El resultado de la multiplicacion es: %s'%str(number))
def divide(request, number1, number2):
    try:
        number = int(number1) / int(number2)
        return HttpResponse('El resultado de la division es: %s'%str(number))
    except ZeroDivisionError:
        return HttpResponse('Has dividido entre 0')
