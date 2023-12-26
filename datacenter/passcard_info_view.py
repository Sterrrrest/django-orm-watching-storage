import datetime

from django.http import Http404
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from get_duration import get_duration
from format_duration import format_duration
  

def is_visit_long(visit, minutes=60):
      duration = get_duration(visit)
      if duration:
          if not duration > datetime.timedelta(minutes=minutes):
              return False
      

def passcard_info_view(request, passcode):
    user = get_object_or_404(Passcard, passcode=passcode)
    this_user_visits = Visit.objects.filter(passcard=user)
    all_this_passcard_visits=[]
    for visit in this_user_visits:
        this_passcard_visits = {
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(visit)
            }
        all_this_passcard_visits.append(this_passcard_visits)
    context = {
        'this_passcard_visits': all_this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)