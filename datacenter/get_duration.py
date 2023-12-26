from django.utils.timezone import localtime

def get_duration(visits):
    for visitors in visits:
        enter = visitors.entered_at
        leave = visitors.leaved_at
        duration = localtime(leave) - localtime(enter)

        return duration