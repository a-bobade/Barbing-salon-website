from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail


def index(request):
    name = ''
    email = ''
    phone = ''
    date = ''
    time = ''
    service = ''
    message = ''

    if request.method == 'POST':
        name = request.POST.get("name", False)
        email = request.POST.get("email", False)
        phone = request.POST.get("phone", False)
        date = request.POST.get("date", False)
        time = request.POST.get("time", False)
        service = request.POST.get("service", False)
        message = request.POST.get("message", False)

        subject = "New Appointment Received"

        comment = "Name: " + name + "\nEmail: " + email + "\nPhone Number: " + phone + "\nDate of Appointment: "\
                  + date + "\nTime of Appointment: " + time + "\nType of Service: " + service + "\n\n\n" + message
        send_mail(subject, comment, email, ['emmaseun95@gmail.com'])

        messages.info(request, 'Thank you, we have received your appointment.')

    return render(request, 'index.html')
