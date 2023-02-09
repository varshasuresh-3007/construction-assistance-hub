import os

from django.core.mail import send_mail

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from construction.settings import EMAIL_HOST_USER


# Create your views here.
def home(request):
    return render(request, 'home.html')


def supclass(request):
    if request.method == 'POST':
        a = supform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["cname"]
            add = a.cleaned_data["address"]
            em = a.cleaned_data["email"]
            ph = a.cleaned_data["phone"]
            us = a.cleaned_data["username"]
            ps = a.cleaned_data["password"]
            b = supreg(cname=nm, address=add, email=em, phone=ph, username=us, password=ps)
            b.save()
            return redirect(suplogclass)

        else:
            return HttpResponse('registration failed')
    else:
        return render(request, 'supplierreg.html')


def suplogclass(request):
    if request.method == 'POST':
        a = suplog(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']
            ps = a.cleaned_data['password']
            b = supreg.objects.all()  # companyname ,address
            for i in b:
                cmp = i.cname
                request.session['cname']=cmp
                cm=i.cname


                # id = i.id
                if i.username == us and i.password == ps:
                    return render(request, 'supprofile.html',{'cm':cm})
                    # return render(request, 'profile.html', {'cmp': cmp, 'id': id})  # wipro #1
            else:
                return HttpResponse('login failed')
    else:
        return render(request, 'suplogin.html')
def supprofile(request):
    return render(request,'supprofile.html')
def matclass(request):
    if request.method=='POST':
        a=matform(request.POST,request.FILES)
        if a.is_valid():
            cm=a.cleaned_data['cname']
            sm=a.cleaned_data['smat']
            img=a.cleaned_data['image']
            nm=a.cleaned_data['nmat']
            qua=a.cleaned_data['quan']
            pr=a.cleaned_data['per']
            pri=a.cleaned_data['price']
            de=a.cleaned_data['des']
            f=matmodel(cname=cm,smat=sm,image=img,nmat=nm,quan=qua,per=pr,price=pri,des=de)
            f.save()
            return redirect(dismat)
        else:
            return HttpResponse('failed')
    else:
        return render(request,'addmaterial.html')


def dismat(request):
    a = matmodel.objects.all()
    b=request.session['cname']
    cm=[]

    sm = []
    img = []
    nm = []
    q = []
    p = []
    pri = []
    d = []
    id1 = []
    for i in a:
        c=i.cname
        cm.append(c)
        s = i.smat
        sm.append(s)
        im = str(i.image).split('/')[-1]
        img.append(im)
        n = i.nmat
        nm.append(n)
        qu = i.quan
        q.append(qu)
        pr = i.per
        p.append(pr)
        pric = i.price
        pri.append(pric)
        de = i.des
        d.append(de)
        id2 = i.id
        id1.append(id2)
    mylist = zip(cm,sm, img, nm, q, p, pri, d,id1)
    return render(request, 'disall.html', {'a': mylist,'b':b})
def userdispro(request):
    a = matmodel.objects.all()
    cm = []

    sm = []
    img = []
    nm = []
    q = []
    p = []
    pri = []
    d = []
    id1=[]

    for i in a:
        c = i.cname
        cm.append(c)
        s = i.smat
        sm.append(s)
        im = str(i.image).split('/')[-1]
        img.append(im)
        n = i.nmat
        nm.append(n)
        qu = i.quan
        q.append(qu)
        pr = i.per
        p.append(pr)
        pric = i.price
        pri.append(pric)
        de = i.des
        d.append(de)
        id2=i.id
        id1.append(id2)

    mylist = zip(cm, sm, img, nm, q, p, pri, d,id1)
    return render(request, 'userdispro.html', {'a': mylist})
def matdelete(request,id):
    a = matmodel.objects.get(id=id)
    a.delete()
    return redirect(dismat)
def matedit(request,id):
    a=matmodel.objects.get(id=id)
    image=str(a.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(a.image) >0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.cname = request.POST.get('cname')
        a.smat=request.POST.get('smat')
        a.nmat=request.POST.get('nmat')
        a.quan=request.POST.get('quan')
        a.per=request.POST.get('per')
        a.price=request.POST.get('price')
        a.des=request.POST.get('des')
        a.save()
        return redirect(dismat)
    return render(request,'matedit.html',{'a':a,'image':image})
def regsupdis(request):
    a=supreg.objects.all()
    return render(request,'regsupdis.html',{'a':a})
def userprofile(request):
    return render(request,'userprofile.html')
def userregclass(request):
    if request.method == 'POST':
        a = userform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data["fname"]
            em = a.cleaned_data["email"]
            add = a.cleaned_data["address"]
            ph = a.cleaned_data["phone"]
            us=a.cleaned_data["username"]
            ps = a.cleaned_data["password"]
            b = userreg(fname=nm,email=em, address=add,  phone=ph,username=us, password=ps)
            b.save()
            return redirect(userlogclass)

        else:
            return HttpResponse('registration failed')
    else:
        return render(request, 'userregister.html')
def userlogclass(request):
    if request.method == 'POST':
        a = userlog(request.POST)
        if a.is_valid():
            us = a.cleaned_data['username']
            ps = a.cleaned_data['password']
            b = userreg.objects.all()  # companyname ,address
            for i in b:
               name=i.fname
               nam=i.fname
               request.session['fname']=nam
               if i.username == us and i.password == ps:
                    return render(request, 'userprofile.html', {'name':name})  # wipro #1
            else:
                return HttpResponse('login failed')
    else:
        return render(request, 'userlogin.html')
def userpro(request):
    a=userreg.objects.all()
    b=request.session['fname']
    return render(request,'viewuserpro.html',{'a':a,'b':b})
# def buyclass(request,id):
#     a=matmodel.objects.get(id=id)
#
#
#     nm=a.nmat
#     pr=a.price
#     if request.method == 'POST':
#         b=buyform(request.POST)
#         if b.is_valid():
#
#             nm=b.cleaned_data['nmat']
#             pri=b.cleaned_data['price']
#             qua=b.cleaned_data['quan']
#             f=buymodel(nmat=nm,price=pri,quan=qua)
#             f.save()
#             return redirect(buynow)
#         else:
#             return HttpResponse('failed')
#     else:
#         return render(request,'buynow.html',{'nm':nm,'pr':pr})
# def finalclass(request):
#
#  a=buymodel.objects.all()
#  nm=a.nmat
#  pr=a.price
#  qu=a.quan
#
#
#  if request.method=='POST':
#      nmat=request.POST.get('nmat')
#      amount=request.POST.get('price')
#      qua=request.POST.get('quan')
#      total=amount * qua
#
#      return HttpResponse('success')
#  return render(request,'final.html',{'total':total,'nm':nm,'pr':pr,'qu':qu})


def edituserprofile(request,id):
    a = userreg.objects.get(id=id)
    if request.method == 'POST':
        a.fname = request.POST.get('fname')
        a.email = request.POST.get('email')
        a.address = request.POST.get('address')
        a.phone = request.POST.get('phone')
        a.username = request.POST.get('username')
        a.password = request.POST.get('password')
        a.save()
        return redirect(userpro)
    return render(request, 'userproedit.html', {'a': a})
def userprofiledel(request,id):
    a = matmodel.objects.get(id=id)
    a.delete()
    return redirect(userpro)
def wishlist(request,id):
    a = matmodel.objects.get(id=id)
    b = wishmodel(cname=a.cname, smat=a.smat, image=a.image, nmat=a.nmat,quan=a.quan,per=a.per,price=a.price,des=a.des)
    b.save()
    return redirect(wishlistalert)
def wishdis(request):
    a = wishmodel.objects.all()
    # b=request.session['cname']
    cm=[]

    sm = []
    img = []
    nm = []
    q = []
    p = []
    pri = []
    d = []
    id1 = []
    for i in a:
        c=i.cname
        cm.append(c)
        s = i.smat
        sm.append(s)
        im = str(i.image).split('/')[-1]
        img.append(im)
        n = i.nmat
        nm.append(n)
        qu = i.quan
        q.append(qu)
        pr = i.per
        p.append(pr)
        pric = i.price
        pri.append(pric)
        de = i.des
        d.append(de)
        id2 = i.id
        id1.append(id2)
    mylist = zip(cm,sm, img, nm, q, p, pri, d,id1)
    return render(request, 'wishdis.html', {'a': mylist})
def macclass(request):
    if request.method == 'POST':
        a = macform(request.POST, request.FILES)
        if a.is_valid():
            cn=a.cleaned_data['cname']

            img = a.cleaned_data['image']
            nm = a.cleaned_data['nmac']
            pri = a.cleaned_data['price']
            pr=a.cleaned_data['per']
            de = a.cleaned_data['des']
            f = macmodel(cname=cn,image=img, nmac=nm, price=pri,per=pr, des=de)
            f.save()
            return redirect(dismac)
        else:
            return HttpResponse('failed')
    else:
        return render(request, 'addmachines.html')


def dismac(request):
    a = macmodel.objects.all()
    b=request.session['cname']

    cn = []
    img = []
    nm = []

    p = []
    pri = []
    d = []
    id1 = []
    for i in a:
        cm = i.cname
        cn.append(cm)
        im = str(i.image).split('/')[-1]
        img.append(im)
        n = i.nmac
        nm.append(n)
        pric = i.price
        pri.append(pric)
        pr = i.per
        p.append(pr)

        de = i.des
        d.append(de)
        id2 = i.id
        id1.append(id2)
    mylist = zip(cn, img, nm,  pri, p, d,id1)
    return render(request, 'macdis.html', {'a': mylist,'b':b})
def buynow(request,id):
    a=buymodel.objects.get(id=id)

    nm=a.nmat
    qu=a.quan
    pr=a.price
    if request.method =='POST':
        amount=int(request.POST.get('price'))
        qua=int(request.POST.get('quan'))
        total=amount*qua
        return render(request,'billnow.html',{'total':total,'nm':nm,'qu':qu,'pr':pr})


    return render(request,'buynow.html',{'a':a})
def supprofiledis(request):
    a=supreg.objects.all()
    b=request.session['cname']
    return render(request,'supprofiledis.html',{'a':a,'b':b})
def supprofiledit(request,id):
    a = supreg.objects.get(id=id)
    if request.method == 'POST':
        a.cname = request.POST.get('cname')
        a.address = request.POST.get('address')
        a.email = request.POST.get('email')
        a.phone = request.POST.get('phone')
        a.username = request.POST.get('username')
        a.password = request.POST.get('password')
        a.save()
        return redirect(supprofiledis)
    return render(request, 'supprofileedit.html', {'a': a})
def supprofiledel(request,id):
    a = userreg.objects.get(id=id)
    a.delete()
    return redirect(supprofiledis)
def confirm(request):
    return render(request,'confirmationalert.html')
def viewbookedpro(request):
    a=buymodel.objects.all()
    return render(request,'viewbookedpro.html',{'a':a})
def confirmessage(request,id):
    a=userreg.objects.get(id=id)
    email=a.email
    fnam=a.fname
    if request.method == 'POST':
        a = messageconfirmform(request.POST)
        if a.is_valid():
            fm=a.cleaned_data['fname']

            em = a.cleaned_data['email']
            me = a.cleaned_data['message']
            # b=confirmmodel(fname=fm,email=em,message=me)
            # b.save()

            subject = f"{fm}"
            message = f" {me}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])

            return redirect(messagealert)
        else:
            return HttpResponse("Details Upload failed!")
    else:
        return render(request,'supmessage.html',{'email':email,'fnam':fnam})
# def finalclass(request,id):
#     a=buynowmodel.objects.get(id=id)
#     cm=a.cname
#     nm = a.nmat
#     qu = a.quan
#     pr = a.price
#     if request.method == 'POST':
#         amount = int(request.POST.get('price'))
#         qua = int(request.POST.get('quan'))
#         total = amount * qua
#         return render(request, 'billnow.html', {'total': total,'cm':cm,'nm': nm, 'qu': qu, 'pr': pr})
#
#     return render(request, 'buynow.html', {'a': a})

def disallmac(request):
    a=macmodel.objects.all()



    cn = []
    img = []
    nm = []

    p = []
    pri = []
    d = []
    # id1 = []
    for i in a:
        cm = i.cname
        cn.append(cm)
        im = str(i.image).split('/')[-1]
        img.append(im)
        n = i.nmac
        nm.append(n)
        pric = i.price
        pri.append(pric)
        pr = i.per
        p.append(pr)

        de = i.des
        d.append(de)
        # id2 = i.id
        # id1.append(id2)
    mylist = zip(cn, img, nm,  pri, p, d)
    return render(request, 'macdisall.html', {'a': mylist})
def messagealert(request):
    return render(request,'messagealert.html')
def editmac(request,id):
    a=macmodel.objects.get(id=id)
    image=str(a.image).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(a.image) >0:
                os.remove(a.image.path)
            a.image=request.FILES['image']
        a.cname = request.POST.get('cname')

        a.nmac=request.POST.get('nmac')

        a.per=request.POST.get('per')
        a.price=request.POST.get('price')
        a.des=request.POST.get('des')
        a.save()
        return redirect(dismac)
    return render(request,'editmac.html',{'a':a,'image':image})
def macdel(request,id):
    a = macmodel.objects.get(id=id)
    a.delete()
    return redirect(dismac)
def viewdetails(request):
    a=macmodel.objects.all()
    return render(request,'viewdetails.html',{'a':a})
def aboutus(request):
    return render(request,'aboutus.html')
def contactus(request):
    return render(request,'contactus.html')
def wishlistalert(request):
    return render(request,'wishlistalert.html')





















