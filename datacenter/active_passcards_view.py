from datacenter.models import Passcard
from django.shortcuts import render


def active_passcards_view(request):
  
    all_passcards = Passcard.objects.all()
    active = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': active,
    }
    return render(request, 'active_passcards.html', context)
