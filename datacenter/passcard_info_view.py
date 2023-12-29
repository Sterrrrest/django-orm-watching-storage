import datetime

from django.http import Http404
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from functions import get_duration
from functions import format_duration
  

def is_visit_long(visit, minutes=60):
  duration = get_duration(visit)
  result = duration > datetime.timedelta(minutes=minutes)
  return result
      

def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    this_user_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits=[]
    for visit in this_user_visits:
        this_passcard_visit = {
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit)
            }
        this_passcard_visits.append(this_passcard_visit)
    context = {
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)