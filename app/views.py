from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request, 'calculator.html')



def result(request):
    num1 = int(request.GET.get('number1'))
    num2 = int(request.GET.get('number2'))

    
    if request.GET.get('add') == "":
        ans = num1 + num2

    elif request.GET.get('subtract') == "":    
        ans = num1 - num2

    elif request.GET.get('multiply') == "":    
        ans = num1 * num2

    else:
        ans = num1 / num2

    return render(request, 'result.html', {'ans': ans})