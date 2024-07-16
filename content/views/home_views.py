from django.shortcuts import render


def home_view(request):
    return render(request, 'content/home.html')


def about_view(request):
    return  render(request, 'content/about.html')


def bio_view(request):
    return render(request, 'content/bio.html')


def resume_view(request):
    return render(request, 'content/resume.html')


def contact_view(request):
    return render(request, 'content/contact.html')