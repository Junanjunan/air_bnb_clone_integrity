import datetime
from django import template
from reservations import models as reservation_models

register = template.Library()


@register.simple_tag
def is_booked(room, day):
    if day.number == 0:
        return
    try:
        date = datetime.datetime(
            year=day.year, month=day.month, day=day.number)
        reservation_models.BookedDay.objects.get(
            day=date, reservation__room=room)
        return True
    except reservation_models.BookedDay.DoesNotExist:
        return False


#  Room.objects.get(host__email="xx@naver.com") --> 호스트의 이메일을 가지고 Room을 찾을수 있는 방법
