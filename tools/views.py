from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, template_name='tools/index.html')


def retirement_calculator_view(request):
    return render(request, template_name='tools/retirement_calculator.html')