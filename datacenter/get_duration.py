from django.utils.timezone import localtime

def get_duration(visit):
  enter = visit.entered_at
  leave = visit.leaved_at
  if leave:
    duration = localtime(leave) - localtime(enter)
    return duration
  else:
    duration = localtime() - localtime(enter)
    return duration