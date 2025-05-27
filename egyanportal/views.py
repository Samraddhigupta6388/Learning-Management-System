from django.shortcuts import render,redirect,HttpResponse
from django.views.decorators.cache import cache_control
from datetime import date
from .models import registration
from django.contrib import messages
from .models import Login
from .models import Usm
from .models import Complaints
from .models import lecture
from .models import assignment
from .models import Feedbacks
from .models import Enquiry
from .models import noti
# Create your views here. 
from django.core.mail import send_mail
#=======================================All methods for template========================================
def layout(request):
    return render(request,'layout.html')
def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def study(request):
    return render(request,'study.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def user_login(request):
    return render(request,'homelogin.html')

def Regi(request):
    return render(request,'rigistration.html')

def about(request):
    return render(request,'about.html')

def studentlayout(request):
    return render(request,'studentlayout.html')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def studenthome(request):
    notif=noti.objects.all()
    lectall=lecture.objects.count()
    assiall=assignment.objects.count()
    allnoti=noti.objects.count()
    usmall=Usm.objects.count()
    if 'userid' in request.session:
        return render(request,'studenthome.html',{'notif':notif,'lectall':lectall,'assiall':assiall,'allnoti':allnoti,'usmall':usmall})
    else:
        return redirect('homelogin')

def adminlogin(request):
    return render(request,'adminlogin.html')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminlayout(request):
    allstudents=registration.objects.count()
    alllecture=lecture.objects.count()
    allusm=Usm.objects.count()
    allassi=assignment.objects.count()
    allfeed=Feedbacks.objects.count()
    allcomp=Complaints.objects.count()
    if 'adminid' in request.session:
        return render(request,'adminlayout.html',{'allstudents':allstudents,'alllecture':alllecture,'allusm':allusm,'allassi':allassi,'allfeed':allfeed,'allcomp':allcomp})
    else:
        return redirect('homelogin')
   
       

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def manageuser(request):
    if 'adminid' in request.session:
        ab=registration.objects.all()
        return render(request,'showdata.html',{'show':ab})
    else:
        return redirect('homelogin')
    
    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def updateprofile(request):
    if 'userid' in request.session:
      user_email=request.session.get('userid')
      user1=registration.objects.filter(email=user_email).first()
      co={
        'uee':user1
       }

      return render(request,'updateprofile.html',co)    
    
    else:
        return redirect('homelogin')
    
   

def viewstudy(request):
    if 'userid' in request.session:
        papa=Usm.objects.all()
        return render(request,'viewstudy.html',{'papa':papa})
    else:
        return redirect('homelogin')
    

def viewlecture(request):
    if 'userid' in request.session:
        lect=lecture.objects.all()
        return render(request,'viewlecture.html',{'lect':lect})
    else:
        return redirect('homelogin')
    

def viewassignment(request):
    if 'userid' in request.session:
        assi=assignment.objects.all()
        return render(request,'viewassignment.html',{'assi':assi})
    else:
        return redirect('homelogin')
    

def complaint(request):
    if 'userid' in request.session:
        sh=registration.objects.all()
        return render(request,'complaint.html',{'S':sh})
    else:
        return redirect('homelogin')
    

def feedback(request):
    if 'userid' in request.session:
        fb=registration.objects.all()
        return render(request,'feedback.html',{'F':fb})
    else:
        return redirect('homelogin')
    
       
@cache_control(no_cache=True,must_revalidate=True,no_store=True) 
def uploadstudy(request):
    if 'adminid' in request.session:
        uppapa=Usm.objects.all()
        return render(request,'uploadstudy.html',{'uppapa':uppapa})
    else:
        return redirect('homelogin')
    
    

def uploadassignments(request):
    if 'adminid' in request.session:
        upassi=assignment.objects.all()
        return render(request,'uploadassignments.html',{'upassi':upassi})
    else:
        return redirect('homelogin')
    
    

def uploadlecture(request):
    if 'adminid' in request.session:
        uplect=lecture.objects.all()
        return render(request,'uploadlecture.html',{'uplect':uplect})
    else:
        return redirect('homelogin')
    
    

def enquiry(request):
    if 'adminid' in request.session:
        en=Enquiry.objects.all()
        return render(request,'enquiry.html',{'en':en})
    else:
        return redirect('homelogin')
    
    

def viewfeedback(request):
    if 'adminid' in request.session:
        fd=Feedbacks.objects.all()
        return render(request,'viewfeedback.html',{'fd':fd})
    else:
        return redirect('homelogin')
    
    

def notification(request):
    if 'adminid' in request.session:
        we=noti.objects.all()
        return render(request,'notification.html',{'we':we})
    else:
        return redirect('homelogin')
    
    

def viewcomplaint(request):
    if 'adminid' in request.session:
        com=Complaints.objects.all()
        return render(request,'viewcomplaint.html',{'com':com})
    else:
        return redirect('homelogin')
    
    

#=======================================All methods for template========================================
#=======================================All methods for Save========================================

def save(request):
    enrollment=request.POST['enrollment']
    name=request.POST['name']
    fname=request.POST['fname']
    mname=request.POST['mname']
    gender=request.POST['gender']
    address=request.POST['address']
    course=request.POST['course']
    branch=request.POST['branch']
    year=request.POST['year']
    mobile=request.POST['mobile']
    email=request.POST['email']
    password=request.POST['password']
    usertype='student'
    status='N'
    a=registration(enrollment=enrollment,name=name,fname=fname,mname=mname,gender=gender,address=address,course=course,branch=branch,year=year,mobile=mobile,email=email,password=password)
    b=Login(userid=email,password=password,usertype=usertype,status=status)
    a.save()
    b.save()
    messages.success(request,'Your data is successfully stored')
    return render(request,'rigistration.html')

def save_view(request):
    if request.method == 'POST':
        # Extract form data
        enrollment = request.POST.get('enrollment')
        name = request.POST.get('name')
        fname = request.POST.get('fname')
        mname = request.POST.get('mname')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        year = request.POST.get('year')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usertype='student'
        status='N'
        a=registration(enrollment=enrollment,name=name,fname=fname,mname=mname,gender=gender,address=address,course=course,branch=branch,year=year,mobile=mobile,email=email,password=password)
        b=Login(userid=email,password=password,usertype=usertype,status=status)
        a.save()
        b.save()
        subject = 'Registration Confirmation'
        message = f'''
        Thank you Your Are Successfuly Register Nou Egyan Protal
        Your Userid And Password This 
        Userid: {email}
        Password: {password}
        '''
        from_email = 'samraddhisatvik@gmail.com'
        recipient_list = [email]
        # Send email
        send_mail(subject, message, from_email, recipient_list)

        # Add success message and redirect
        messages.success(request, 'Registration successful! Please check your email for confirmation.')
        return render(request,'rigistration.html') # Replace with your success URL

    return render(request,'rigistration.html')
def logcode(request):   
    if request.method=="POST":
       userid=request.POST['userid']
       password=request.POST['password']
       usertype=request.POST['usertype']
       ad=Login.objects.filter(userid=userid,password=password).first()
       if ad:
           if ad.usertype=="student" and usertype=="student":
               request.session['userid']=userid
               return redirect('studenthome')
           elif ad.usertype=="admin" and usertype=="admin":
               request.session['adminid']=userid
               return redirect('adminlayout')  
           else:
               messages.success(request,'Invalid User')
               return redirect('homelogin')
       else:
           messages.success(request,'Invalid User')
           return render(request,'homelogin.html')

def usmsave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    new_file = request.FILES['new_file']
    sv = Usm(program=program,Branch=Branch,Year=Year,subject=subject,file_name=file_name,new_file=new_file)
    sv.save()
    messages.success(request,'Study Material Successfully Save')
    return redirect('uploadstudy')

def Complaintsave(request,id):
    sg=registration.objects.get(pk=id)
    Subject=request.POST['Subject']
    comp=request.POST['comp']
    status='Pending'
    reqdate=date.today()
    v=Complaints(name=sg.name,program=sg.course,branch=sg.branch,contactno=sg.mobile,email=sg.email,Subject=Subject,comp=comp,reqdate=reqdate,status=status)
    v.save()
    messages.success(request,'Complaint uploaded successfully')
    return redirect('complaint')

def lecturesave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    link = request.POST['link']
    pt = lecture(program=program,Branch=Branch,Year=Year,subject=subject,file_name=file_name,link=link)
    pt.save()
    messages.success(request,'Links Uploaded Successfully')
    return redirect('uploadlecture')

def assisave(request):
    program = request.POST['program']
    Branch = request.POST['Branch']
    Year = request.POST['Year']
    subject = request.POST['subject']
    file_name = request.POST['file_name']
    new_file = request.FILES['new_file']
    sv = assignment(program=program,Branch=Branch,Year=Year,subject=subject,file_name=file_name,new_file=new_file)
    sv.save()
    messages.success(request,'Assignments uploaded')
    return redirect('uploadassignments')

def Feedbacksave(request,id):
    pr=registration.objects.get(pk=id)
    Subject=request.POST['Subject']
    feed=request.POST['feed']
    status='Pending'
    reqdate=date.today()
    w=Feedbacks(name=pr.name,program=pr.course,branch=pr.branch,status=status,contactno=pr.mobile,email=pr.email,Subject=Subject,feed=feed,reqdate=reqdate)
    w.save()
    messages.success(request,'Feedback uploaded successfully')
    return redirect('feedback')

def enqsave(request):
    name=request.POST['name']
    contactno=request.POST['contactno']
    email=request.POST['email']
    enq=request.POST['enq']
    enqdate=date.today()
    ens=Enquiry(name=name,contactno=contactno,email=email,enq=enq,enqdate=enqdate)
    ens.save()
    messages.success(request,'Enquiry Submitted')
    return redirect('contact')

def notisave(request):
    notim=request.POST['notim']
    notidate=date.today()
    ns=noti(notim=notim,notidate=notidate)
    ns.save()
    return redirect('notification')

#=======================================All methods for Save========================================
#======================================All Delete ===============================================

def deleteUsm(request,id):
    usd=Usm.objects.get(pk=id)
    usd.delete()
    return redirect('uploadstudy')

def deleteuser(request,id):
    duser=registration.objects.get(pk=id)
    duser.delete()
    return redirect('showdata')

def deletelect(request,id):
    dlect=lecture.objects.get(pk=id)
    dlect.delete()
    return redirect('uploadlecture')

def deleteassi(request,id):
    dassi=assignment.objects.get(pk=id)
    dassi.delete()
    return redirect('uploadassignments')

def logout(request):
    request.session.flush()
    return redirect('home')

#======================================All Delete ===============================================
#======================================All Update ===============================================
def updatedata(request,id):
    qw=registration.objects.get(pk=id)
    return render(request,'updatedata.html',{'qw':qw})

def updateform(request):
    if request.method=='POST':
        enrollment=request.POST['enrollment']
        name=request.POST['name']
        fname=request.POST['fname']
        mname=request.POST['mname']
        gender=request.POST['gender']
        address=request.POST['address']
        course=request.POST['course']
        branch=request.POST['branch']
        year=request.POST['year']
        mobile=request.POST['mobile']
        email=request.POST['email']
        password=request.POST['password']
        a=registration(enrollment=enrollment,name=name,fname=fname,mname=mname,gender=gender,address=address,course=course,branch=branch,year=year,mobile=mobile,email=email,password=password)
        a.save()
        return redirect('showdata')
    
def updatepro(request):
    user_email=request.session.get('userid')
    user=registration.objects.filter(email=user_email).first()
    con={
        'ue':user
    }
    return render(request,'updatepro.html',con)

def upsave(request):
    if request.method == 'POST':
        user_email = request.session.get('userid')
        user = registration.objects.filter(email=user_email).first()

        if user:
            user.enrollment = request.POST['enrollment']
            user.name = request.POST['name']
            user.fname = request.POST['fname']
            user.mname = request.POST['mname']
            user.gender = request.POST['gender']
            user.address = request.POST['address']
            user.course = request.POST['course']
            user.branch = request.POST['branch']
            user.year = request.POST['year']
            user.mobile = request.POST['mobile']
            user.email = request.POST['email']
            user.password = request.POST['password']

            if 'New_file' in request.FILES:
                user.New_file = request.FILES['New_file']

            user.save()
            return redirect('updateprofile')
        else:
           
             return redirect('updateprofile')
   






       

       





