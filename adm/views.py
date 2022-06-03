from home.models import *
from home import *
from django.shortcuts import render, redirect


def ah(request):
    return render(request, 'adm/AdminLand.html')


def NoticeList(request):
    if request.method == "GET":
        notice = Notice.objects.all()
        context = {
            'notice': notice
        }
    return render(request, 'adm/ANotice.html', context)


def action_handler(request, action, id):
    if action == 'delete':
        notice = Notice.objects.get(id=id)
        notice.delete()

    elif action == 'edit':
        if request.method == 'GET':
            notice = Notice.objects.get(id=id)
            context = {
                'notice': notice
            }
            return render(request, 'adm/NUpdate.html', context)

        if request.method == 'POST':
            input_notice = request.POST["notice"]

            notice = Notice.objects.get(id=id)

            notice.notice = input_notice
            notice.save()
    return redirect('/noticelist/')


def Rinfo(request):
    if request.method == "GET":
        reg = Reg.objects.all()
        context = {
            'reg': reg
        }
        return render(request, 'adm/AReginfo.html', context)


def act_handler(request, action, id):
    if action == 'delete':
        reg = Reg.objects.get(id=id)
        reg.delete()

    elif action == 'edit':
        if request.method == 'GET':
            reg = Reg.objects.get(id=id)
            context = {
                'reg': reg
            }
            return render(request, 'adm/RUpdate.html', context)
        if request.method == 'POST':
            input_firstname = request.POST["firstname"]
            input_lastname = request.POST["lastname"]
            input_phone = request.POST["phone"]
            input_email = request.POST["email"]

            reg = Reg.objects.get(id=id)

            reg.firstname = input_firstname
            reg.lastname = input_lastname
            reg.phone = input_phone
            reg.email = input_email

            reg.save()
    return redirect('/userinfo')


def newNotice(request):
    if request.method == "GET":
        addnew = Notice.objects.all()
        context = {
            'addnew': addnew
        }
        return render(request, 'adm/New Notice.html', context)

    elif request.method == "POST":
        notice = request.POST["notice"]

        Notice.objects.create(notice=notice)
    return redirect('/noticelist/',)
