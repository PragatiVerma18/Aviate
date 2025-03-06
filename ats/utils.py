import pytz

from django.utils import dateformat
from django.utils.html import format_html


def truncated_uuid(value):
    if not value:
        return None
    truncated_value = str(value)[-12:]
    return format_html(f'<span title="{value}">{truncated_value}</span>')


def datetime_ist(utc_datetime_obj):
    return utc_datetime_obj.replace(tzinfo=pytz.utc).astimezone(
        pytz.timezone("Asia/Kolkata")
    )


def datetime_format(datetime_obj, output_format="N j, Y, f a"):
    df = dateformat.DateFormat(datetime_obj)
    return df.format(output_format)


def datetime_format_ist(utc_datetime_obj):
    if not utc_datetime_obj:
        return None
    ist_datetime_obj = datetime_ist(utc_datetime_obj)
    return datetime_format(ist_datetime_obj)
