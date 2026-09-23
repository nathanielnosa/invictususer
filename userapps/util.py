from django.core.mail import send_mail
from django.conf import settings

def sendEmail(username,email):
    subject = "Welcome to Invictus app"
    body = f'''
        welcome {username}!
        This is an onboarding message from the team
    '''
    
    send_mail(
        subject,
        body,
        from_email=settings.MAILERS["username"],
        recipient_list=[email]
        ["email"],
         fail_silently=False,
    )
