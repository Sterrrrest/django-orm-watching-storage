from django.utils.timezone import localtime

def format_duration(duration):
    hours = round(duration.total_seconds() // 3600)
    minutes = round(duration.total_seconds() // 60)
    time = f'{hours}ч {minutes}мин'
    return time