from django.utils.timezone import localtime

def format_duration(duration):
    sec_in_hour = 3600
    sec_in_min = 60
    hours = round(duration.total_seconds() // sec_in_hour)
    minutes = round(duration.total_seconds() // sec_in_min) % sec_in_min
    time = f'{hours}ч {minutes}мин'
    return time


def get_duration(visit):
  enter = visit.entered_at
  leave = visit.leaved_at
  if leave:
    duration = localtime(leave) - localtime(enter)
    return duration
  else:
    duration = localtime() - localtime(enter)
    return duration