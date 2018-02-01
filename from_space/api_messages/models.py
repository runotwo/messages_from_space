from django.db import models
from django.forms.models import model_to_dict
import datetime


class Message(models.Model):
    date = models.DateField(default=datetime.date.today)
    text = models.TextField(default='')
    is_read = models.BooleanField(default=False)

    @classmethod
    def get_latest(cls, id):
        resp = [model_to_dict(x) for x in list(cls.objects.filter(id__gt=id).exclude(is_read=1))]
        for x in resp:
            print(x)
            if x.get('date'):
                x['date'] = x['date'].strftime('%d/%m/%Y')
            else:
                x['date'] = ''
        return resp
