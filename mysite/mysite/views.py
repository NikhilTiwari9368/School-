from dataclasses import dataclass
from email import message
from django.http import HttpRequest, HttpResponse , HttpResponseRedirect
from django.shortcuts import redirect, render 
from .forms import userForm
from Service.models import Services
from news.models import News 
from django.core.paginator import Paginator 
# from django.core.mail import send_mail , EmailMultiAlternatives

def homePage(request):
    # subject ='Testing mail'
    # from_mail = 'nikhilcoder123.gmail.com'
    # msg = '<p> welcome to <b>gvm</b></p>'
    # to='nikhiltiwari9368@gmail.com'
    # msg=EmailMultiAlternatives(subject , msg , from_mail ,[to])
    # msg.content_subtype='html'
    # msg.send()


    newsdata = News.objects.all(); 
    servicedata = Services.objects.all().order_by('-service_title')

    data={
        'servicedata' : servicedata,
        'newsdata' : newsdata
    }
    # for a in servicedata:
    #     print(a.service_icon)
    return render(request , "index.html" , data)

def newsDetails(request , newsid ):
    newsDetails = News.objects.get(id = newsid )
    data={
        'newsDetails' : newsDetails
    }
    return render(request , "newsdata.html")

def about(request):
    if request.method == "GET":
        output=request.GET.get('output')
    return render(request , "about.html",{'output':output})

def contact(request):
    finalans=0
    fn=userForm() 
    data={'form':fn}
    try:
        if request.method == "POST":
        # n1=int(request.GET['num1])
        # n1=int(request.GET['num2])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))   
            finalans = n1+n2
            data={
                'form':fn,
                'output' : finalans
            }

            url="/about/?output={}" .format(finalans)
            return redirect(url)

    except:
        pass

    return render(request , "contact.html" ,data)

def submitform(request):
    try:
        if request.method == "POST":
        # n1=int(request.GET['num1])
        # n1=int(request.GET['num2])
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))   
            finalans = n1+n2
            data={
                'n1' : n1,
                'n2' : n2,
                'output' : finalans
            }
    
            return HttpResponse(finalans)
    except:
        pass

def calculator(request):
    c=''
    data={}
    n1=''
    n2=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')

            data={'n1':n1 ,
                    'n2':n2 ,
                    'opr':opr}

            if opr=="+":
                c=n1+n2
            
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            
            elif opr=="/":
                c=n1/n2

    except:
        c="Invalid operation"
    print(c)
    return render(request,"calculater.html",{'c':c})

def evenodd(request):
    c=''
    if request.method == "POST" :
        if request.POST.get('num1')=="":
            return render(request,"evenodd.html",{'error' : True})
            
        n=eval(request.POST.get('num1'))

        if n%2 == 0:
             c="Even Number"
        else:
            c="Odd Number"

    print(c)
    return render(request,"evenodd.html",{'c':c})

def sport(request):
    return render(request,"sport.html")


def Libarary(request):
    return render(request ,"Libaray.html")

def interactive(request):
    return render(request,"interactive.html")

def admission(request):
    return render(request,"admission.html")

def mission(request):
    return render(request ,"mission.html")

# def saveEnquiry(request):
#     if request.method == "POSt":

#     return render(request ,"contact.html")

# def service(request):
#     ServiceData = Service.objects.all()
#     paginator = Paginator(ServiceData,2)
#     page_number = request.GET.get('page')
#     ServiceDatafinal = paginator.get_page(page_number)
