from django.shortcuts import render
from .models import *
from django.template import loader
from django.http import HttpResponseRedirect


# Create your views here.

def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def registerform(request):
    return render(request,'register.html')

def single(request):
    return render(request,'single.html')

def home(request):
    return render(request,'homepage.html')

def empregister(request):
    return render(request,"empregister.html")


# def login1(request):
#     if request.method=="POST":
#         lemail=request.POST['email'] 
#         lpassword=request.POST['password'] 
#         check=login.objects.filter(email=lemail,password=lpassword)
#         if check:
#             for x in check:
#                 request.session["uid"]=x.id
#             return render(request,'login.html')
#         else:
#             return render(request,'login.html',{"err123":"unregistered, please register"})
#     else:
#             return render(request,'login.html')


# employee details registration form
# ------------------------------------

def regform1(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        qualification=request.POST["qualification"]
        experiance=request.POST["experience"]
        linkdlnpro=request.POST["linkedin"]
        jobcat=request.POST["jobcategory"]
        # resume=request.FILES["resume"]

        check=regform.objects.filter(email= email)
        if check:
            return render(request,"employee_form.html",{"error":"email already registered"})
        else:
            add=regform(name=name,email=email,phone=phone,qualification=qualification,experiance=experiance,linkdlnpro=linkdlnpro,jobcat=jobcat)
            add.save()
            return render(request,"employee_form.html",{"success":"Saved"})
    else:
        return render(request,"employee_form.html")
    


def emp_reg_view1(request):
    if request.session.has_key('id'):
        mydata=regform.objects.all()
        return render(request,"admin/emp_reg_view.html",{"data124":mydata})
    else:
        return render(request,"admin/emp_reg_view.html")
    


def userdelete2(request):
    uid=request.GET['uuid']
    mydata=regform.objects.filter(id=uid).delete()
    return HttpResponseRedirect("/emp_reg_view1/")

# register details update
# -------------------------

def userupdate2(request):
    if request.method == "POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        qualification=request.POST["qualification"]
        experiance=request.POST["experience"]
        linkdlnpro=request.POST["linkedin"]
        jobcat=request.POST["jobcategory"]

        uid=request.GET['uuid']
        add=regform.objects.filter(id=uid).update(name=name,email=email,phone=phone,qualification=qualification,experiance=experiance,linkdlnpro=linkdlnpro,jobcat=jobcat)
        return HttpResponseRedirect("/emp_reg_view1/")
    else:
        uid=request.GET['uuid']
        mydata=regform.objects.filter(id=uid)
        return render(request,"admin/emp_reg_update.html",{"data124":mydata})
    

# ---------------------------------------------------------------------------------------


def index2(request):
        return render(request,"admin/index2.html")


# employer login form
# ----------------------------

def emp_login_form(request):
    if request.method=="POST":
        lemail=request.POST['loemail'] 
        lpassword=request.POST['lopass'] 
        check=adregisterform.objects.filter(aemail=lemail,passwd=lpassword)
        if check:
            for x in check:
                request.session["uid"]=x.id
                request.session["name"]=x.afname
            return render(request,'index.html')
        else:
            return render(request,'login.html',{"err123":"unregistered, please register"})
    else:
        return render(request,'login.html')
    

# employee registration form
# -----------------------------

def adregisterform1(request):
    if request.method=="POST":
        afname=request.POST['fname'] 
        alname=request.POST['lname'] 
        aemail=request.POST['email'] 
        passwd=request.POST['passwd'] 
        cpasswd=request.POST['cpasswd'] 
        check=adregisterform.objects.filter(aemail=aemail)
        if passwd==cpasswd:
            if check:
                    return render(request,"register.html",{"error":"email already registered"})
            else:
                add=adregisterform(afname=afname,alname=alname,aemail=aemail,passwd=passwd,cpasswd=cpasswd)
                add.save()
                return render(request,"login.html",{"success":"saved"})
        else:
             return render(request,"register.html",{"error1":"Password Dosen't match!!!"})
    else:
        return render(request,"register.html")
    

# employer logout form
# -----------------------


def logout1(request):
    if request.session.has_key('uid'):
        del request.session["uid"]
        del request.session["name"]
        return HttpResponseRedirect("/")


    






# ----------------------ADMIN-----------------------------------


# admin registration formm
# -----------------------------------

def ad_login_form(request):
    if request.method=="POST":        
        lemail=request.POST['lemail']
        lpassword=request.POST['lpassword']        
        check=admin_login.objects.filter(email=lemail,passw=lpassword)
        if check:
            for x in check:
                request.session["id"]=x.id
            return render(request,"admin/index2.html")
        else:            
            return render(request,"admin/ad_login_form.html",{"err":"Unregistered"})
    else:
        return render(request,'admin/ad_login_form.html')



def basic_table(request):
    if request.session.has_key('id'):
        mydata=adregisterform.objects.all()
        return render(request,"admin/basic_table.html",{"data12":mydata})
    else:
        return render(request,"admin/basic_table.html")


def index2(request):
        return render(request,"admin/index2.html")


# user delete by admin
# ---------------------
  
def userdelete(request):
    uid=request.GET['uuid']
    mydata=adregisterform.objects.filter(id=uid).delete()
    return HttpResponseRedirect("/basic_table/")

# user update by admin
# ---------------------------

def userupdate(request):
    if request.method == "POST":
        afname1=request.POST["fname"]
        alname1=request.POST["lname"]
        aemail1=request.POST["email"]
        passwd1=request.POST["passwd"]
        cpasswd1=request.POST["cpasswd"]
        uid=request.GET['uuid']
        add=adregisterform.objects.filter(id=uid).update(afname=afname1,alname=alname1,aemail=aemail1,passwd=passwd1,cpasswd=cpasswd1)
        print("haiii")
        return HttpResponseRedirect("/basic_table/")
    else:
        uid=request.GET['uuid']
        mydata=adregisterform.objects.filter(id=uid)
        return render(request,"admin/update.html",{"data12":mydata})
    





  
  
    













































































































































































































































































































