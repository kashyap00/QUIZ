from django.shortcuts import render , HttpResponse
from datetime import datetime
from quizapp.models import Student
from quizapp.models import Employee


# Create your views here.
def index(request):
    return render(request,'index.html')
    #return HttpResponse ("this my first page")
def startquiz(request):
    return HttpResponse ("star quiz in a min")   

def candidate(request):
    if request.method=="POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        email = request.POST.get('email')
        password =request.POST.get('password')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        
        student = Student( firstname=firstname,lastname=lastname,email=email,password=password, address1=address1 ,address2=address2 ,state= state, city=city ,zip=zip,date=datetime.today())
        #candidate = Candidate(firstname='firstname', lastname='lastname', email='email', address1='address1' ,address2='address2' ,state= 'state', city='city' ,zip='zip',date=datetime.today())
        student.save()
    return render(request,'candidate.html')

    #return HttpResponse("Candidate login")
def questionmaker(request):
    if request.method  =="POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        state = request.POST.get('state')
        city = request.POST.get('city')
        zipc = request.POST.get('zipc')
       
        questionmaker = Employee(firstname=firstname,lastname=lastname, email=email,password=password, address1= address1,address2=address2 ,state= state, city=city ,zipc=zipc,date=datetime.today())
        questionmaker.save()
    return render(request,'question maker.html')
    #return HttpResponse("question maker")  
def login(request):
    return render(request,'login.html')
    #return HttpResponse("login here")    