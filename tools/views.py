from django.contrib.auth.decorators import login_not_required
from django.shortcuts import render

from tools.forms import RetirementCalculatorForm


# Create your views here.
@login_not_required
def index_view(request):
    return render(request, template_name='tools/index.html')


@login_not_required
def retirement_calculator_view(request):
    form = RetirementCalculatorForm()
    context = {'form': form}
    return render(request, template_name='tools/retirement_calculator.html', context=context)


@login_not_required
def theme_view(request):
    template_name = 'tools/theme.html'
    colors = ['base', 'muted', 'primary', 'secondary', 'tertiary', 'accent', 'error', 'success', 'link', 'link-hover', 'link-active',
              'info', 'warning']
    themes = ['light', 'dark']
    context = {'themes': themes, 'colors': colors}
    return render(request, template_name=template_name, context=context)


@login_not_required
def css_display_cheatsheet_view(request):
    template_name = 'tools/css_display_cheatsheet.html'
    context = dict()
    return render(request, template_name=template_name, context=context)
