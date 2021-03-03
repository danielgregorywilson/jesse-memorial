from django.core.mail import send_mail


def get_host_url(request):
    host = request.get_host()
    if request.is_secure():
        return f'https://{ host }/'
    else:
        return f'http://{ host }/' 


def send_email(to_address, subject, body, html_body):
    print("SENT EMAIL TO:", to_address)
    return send_mail(subject, body, 'dwilson@lcog.org', [to_address], html_message=html_body)


def is_true_string(str):
    if str in ['true', 'True']:
        return True
    return False