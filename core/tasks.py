from django.conf import settings
from django.template import loader
from celery import shared_task
from .models import HalfHourData

@shared_task()
def save_data(duration):
    tkt = Ticket.objects.get(pk=tkt_id)
    html_message = loader.render_to_string(
        'tickets/email.html',
        {
            'title': tkt.title,
            'content':tkt.content,
            'code':tkt.code,
            'sender':tkt.created_by,
            'receiver':tkt.assigned_to,
        }
        )
    send_email.delay(tkt.title, tkt.content,tkt.created_by.email,tkt.assigned_to.email, html_message)