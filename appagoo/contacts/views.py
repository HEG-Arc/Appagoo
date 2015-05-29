from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from models import ContactForm
from django.template import RequestContext
from django.core.mail import send_mail, BadHeaderError


def contactview(request):
    subject = request.POST.get('topic', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')

    if subject and message and from_email:
            try:
                send_mail(subject, message, from_email, ['alessio.desanto@gmail.com'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thankyou/')
    else:
        return render_to_response('contacts.html', RequestContext(request, {'form': ContactForm()}))

    return render_to_response('contacts.html', RequestContext(request, {'form': ContactForm()}), RequestContext(request))


def thankyou(request):
    return render_to_response('thankyou.html', RequestContext(request, {}))