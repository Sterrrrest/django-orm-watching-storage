from django.utils.timezone import localtime

def format_duration(duration):
    SEC_IN_HOUR = 3600
    MIN_IN_HOUR = 60
    hours = round(duration.total_seconds() // SEC_IN_HOUR)
    minutes = round(duration.total_seconds() // MIN_IN_HOUR)
    time = f'{hours}ч {minutes}мин'
    return time