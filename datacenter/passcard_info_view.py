import datetime

from django.http import Http404
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
  enter = visit.entered_at
  leave = visit.leaved_at
  if leave:
    duration = localtime(leave) - localtime(enter)
    return duration
    

def format_duration(duration):
  hours = round(duration.total_seconds() // 3600)
  minutes = round(duration.total_seconds() // 60)%60
  time = f'{hours}ч {minutes}мин'
  return time
  

def is_visit_long(visit, minutes=60):
  duration = get_duration(visit)
  if duration:
    if duration > datetime.timedelta(minutes=minutes):
      return True
    else:
      return False
      

def passcard_info_view(request, passcode):
    try:
        user = Passcard.objects.get(passcode=passcode)
    except Passcard.DoesNotExist:
        raise Http404()
    this_user_visits = Visit.objects.filter(passcard=user)
    all_this_passcard_visits=[]
    for visit in this_user_visits:
        entered_at = visit.entered_at
        duration = format_duration(get_duration(visit))
        is_strange = is_visit_long(visit)
               
        this_passcard_visits = {
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': is_strange
            }
        all_this_passcard_visits.append(this_passcard_visits)
    context = {
        'this_passcard_visits': all_this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)