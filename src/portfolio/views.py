from django.shortcuts import render

from .models import Portfolio


def home(request):
    if not Portfolio.objects.filter(is_active=True).exists():
        return render(request, 'portfolio/error.html')

    portfolio = Portfolio.objects.filter(is_active=True).order_by('-updated').first()
    social_medias = portfolio.social_medias.all()
    contacts = portfolio.contacts.all()

    context = {
        'portfolio': portfolio,
        'social_medias': social_medias,
        'contacts': contacts
    }

    return render(request, 'portfolio/portfolio.html', context)
