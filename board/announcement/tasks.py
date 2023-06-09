from celery import shared_task
from .models import Post, User
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from board.settings import DEFAULT_FROM_EMAIL


@shared_task
def action():
    new_post = Post.objects.filter(article_time_in__gt=datetime.now() - timedelta(days=1))
    list_of_emails = []
    for user in User.objects.all():
        list_of_emails.append(user.email)
    html_context = {'new_post': new_post}
    html_content = render_to_string('news_notification.html', html_context)
    msg = EmailMultiAlternatives(
        subject='Новые объявления на сайте',
        from_email=DEFAULT_FROM_EMAIL,
        to=list_of_emails
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
