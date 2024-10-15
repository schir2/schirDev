from django.shortcuts import render

from tools.forms import RetirementCalculatorForm


# Create your views here.
def index_view(request):
    return render(request, template_name='tools/index.html')


def retirement_calculator_view(request):
    form = RetirementCalculatorForm()
    context = {'form': form}
    return render(request, template_name='tools/retirement_calculator.html', context=context)