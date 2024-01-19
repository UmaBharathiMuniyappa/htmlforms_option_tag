from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        QLWO=Webpage.objects.all()
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        na=request.POST['na']
        da=request.POST['da']
        au=request.POST['au']
        WO=Webpage.objects.get(pk=na)
        AO=AccessRecord.objects.get_or_create(name=WO,date=da,author=au)[0]
        AO.save()
        QLAO=AccessRecord.objects.all()
        d1={'accessrecord':QLAO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'insert_accessrecord.html',d)

def select_multiple_webpage(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for i in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=i)
        d1={'webpages':QLWO}
        return render(request,'display_webpage.html',d1)

    return render(request,'select_multiple_webpage.html',d)

def select_multiple_access(request):
    QLWO=Webpage.objects.all()
    d={'webpages':QLWO}
    if request.method=='POST':
        namelist=request.POST.getlist('na')
        QLAO=AccessRecord.objects.none()
        for j in namelist:
            QLAO=QLAO|AccessRecord.objects.filter(name=j)
        d1={'accessrecord':QLAO}
        return render(request,'display_accessrecord.html',d1)
    return render(request,'select_multiple_access.html',d)

def checkbox(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        topiclist=request.POST.getlist('tn')
        QLWO=Webpage.objects.none()
        for tn in topiclist:
            QLWO=QLWO|Webpage.objects.filter(topic_name=tn)
        d1={'webpage':QLWO}
        return render(request,'display_webpage.html',d1)
    return render(request,'checkbox.html',d)