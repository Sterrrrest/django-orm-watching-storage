from django.db.models.fields import duration_string

from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime

def get_duration(visits):

    for visitors in visits:
        enter = visitors.entered_at
        leave = visitors.leaved_at
        duration = localtime(leave) - localtime(enter)
      
        return duration  
  
def format_duration(duration):
    hours = round(duration.total_seconds() // 3600)
    minutes = round(duration.total_seconds() // 60)
    time = f'{hours}ч {minutes}мин'
    return time
  
def storage_information_view(request):
    visits = Visit.objects.all()
    users_not_leaved = Visit.objects.filter(leaved_at=None)
    all_visits = []
  
    for visitors in users_not_leaved:
        who_entered = visitors.passcard.owner_name
        enter = visitors.entered_at
        duration = format_duration(get_duration(visits))
        non_closed_visits = {
                'who_entered': who_entered,
                'entered_at': enter,
                'duration': duration,
            }
        
        all_visits.append(non_closed_visits)
    context = {
          'non_closed_visits': all_visits,
      }
    return render(request, 'storage_information.html', context)
