from home.models import *
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from home.form import ContactForm


def hm(request):
    return render(request, 'home/home.html')


def land(request):
    return render(request, 'home/home 2.html')


def registration(request):
    if request.method == "GET":
        reg = Reg.objects.all()
        context = {
            'registration': Reg
        }
        return render(request, 'home/registration.html', context)

    elif request.method == "POST":
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        sid = request.POST["sid"]
        phone = request.POST["phone"]
        email = request.POST["email"]
        password = request.POST["password"]
        
        Reg.objects.create(firstname=firstname, lastname=lastname, sid=sid, phone=phone, email=email, password=password)
    return redirect('/', )


def rs(request):
    if request.method == "GET":
        result = Result.objects.all()
        context = {
            'result': result
        }
    return render(request, 'home/result.html', context)


def pay(request):
    if request.method == "GET":
        payment = Payment.objects.all()
        context = {
            'payment': payment
        }
    return render(request, 'home/Payment.html', context)


def noti(request):
    if request.method == "GET":
        notice = Notice.objects.all()
        context = {
            'notice': notice
        }
    return render(request, 'home/Notice.html', context)


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['contact.anisujjaman@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        return redirect('/land')
    return render(request, "home/Contact.html", {'form': form})
