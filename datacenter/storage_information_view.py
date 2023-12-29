from django.db.models.fields import duration_string
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from get_duration import get_duration
from format_duration import format_duration
  
def storage_information_view(request):
    visits = Visit.objects.all()
    visits_not_leaved = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
  
    for visitors in visits_not_leaved:
        who_entered = visitors.passcard.owner_name
        enter = visitors.entered_at
        duration = format_duration(get_duration(visitors))
        non_closed_visits = {
                'who_entered': who_entered,
                'entered_at': enter,
                'duration': duration,
            }
        
        non_closed_visits.append(non_closed_visits)
    context = {
          'non_closed_visits': non_closed_visits,
      }
    return render(request, 'storage_information.html', context)
