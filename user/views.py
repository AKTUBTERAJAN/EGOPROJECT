from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def index(request):
    sdata=slider.objects.all().order_by('-id')[0:3]
    uedata=upcomingevents.objects.all().order_by('-id')[0:8]
    vdata = volunteer.objects.all().order_by('email')[0:12]
    ddata=donateus.objects.all().order_by('-id')[0:12]
    mydict={"sd":sdata,"uedata":uedata,"vdata":vdata,"ddata":ddata}
    vdata=volunteer.objects.all().order_by('email')[0:12]
    return render(request,'user/index.html',mydict)

def about(request):
    return render(request,'user/about.html')

def contact(request):
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('mobile')
        d=request.POST.get('msg')
        contact(name=a,email=b,mobile=c,msg=d).Save()
        return HttpResponse("<script>alert('thanks for contacting with us...');location.href='/user/contact/'</script>")
    return render(request,'user/contact.html')

def ourvolunteers(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        address=request.POST.get('address')
        cposition=request.POST.get('cposition')
        picture=request.FILES['fu']
        x=volunteer.objects.filter(email=email).count()#
        if x==0:
            volunteer(name=name,email=email,mobile=mobile,city=address,current_position=cposition,picture=picture).save()
            return HttpResponse("<script>alert('you are registered successfully..');location.href='/user/volunteer/'</script>")
        else:
            return HttpResponse("<script>alert('you are already registered..');location.href='/user/volunteer/'</script>")
    return render(request,'user/volunteer.html')

def login(request):
    return render(request,'user/login.html')

def vissionmission(request):
    return render(request,'user/vission mission.html')

def upevent(request):
    return render(request,'user/event.html')

def viewevent(request):
    eid=request.GET.get('msg')
    data=upcomingevents.objects.filter(id=eid)
    md={"data":data}
    return render(request,'/user/viewevent.html',md)

def event(request):
    data=upcomingevents.objects.all().order_by('-id')
    md={"edata":data}
    return render(request,'user/event.html',md)

def donatenow(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        picture=request.POST.get('fu')
        city=request.POST.get('city')
        pincode=request.POST.get('pincode')
        amount=request.POST.get('amount')
        address=request.POST.get('address')
        donateus(name=name,picture=picture,mobile=mobile,email=email,city=city,address=address,pincode=pincode,rupees=amount,ddate=datetime.now().date()).save()
        return HttpResponse("<script>alert('thanks for donate now...');location.href='/user/donatenow/'</script>")
    return render(request,'user/donatenow.html')
def  help(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        picture=request.POST.get('fu')
        htype=request.POST.get('helptype')
        message=request.POST.get('message')
        address=request.POST.get('address')
        nhelp(name=name,mobile=mobile,helptype=htype,message=message,address=address,picture=picture,request_date=datetime.now().date()).save()
        return HttpResponse("<script>alert('your request added successfully...');location.href='/user/help/'</script>")
    return render(request,'user/help.html')

def  story(request):
    scdata=schange.objects.all().order_by('-id')
    md={"scdata":scdata}
    return render(request,'user/stories & change.html',md)

def volunteerslist(request):
    vid=request.GET.get('vid')
    did=request.GET.get('did')
    ddata="";
    vdata="";
    if vid is not None:
        vdata=volunteer.objects.filter(email=vid)
    elif did is not None:
        ddata=donateus.objects.filter(id=did)
    else:
        vdata=volunteer.objects.all()
        ddata=donateus.objects.all().order_by('-id')
    md={
        "vdata":vdata,
        "ddata":ddata
    }
    return render(request,'user/volunteerlist.html',md)