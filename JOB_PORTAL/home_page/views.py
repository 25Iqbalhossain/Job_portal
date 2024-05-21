
from django.shortcuts import render, HttpResponse, redirect
from home_page.models import Comsingup, Comlogin,Candidatesingup
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def index(request):
  if request.user.is_anonymous:
    return redirect('/login')
  return render(request,'index.html')

def authView(request):
  if request.method =="POST":
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
      form.save()
  else:
   form=UserCreationForm()
  return render(request,'registration/comsingup.html',{"form":form})
def jobs(request):
  return render(request,'jobs.html')
  #return HttpResponse("THIS IS A PROJECT JOBS PAGE")

def candidates(request):
  return render(request,'candidates.html')
  #return HttpResponse("THIS IS A PROJECT CANDIDATE PAGE")

def company(request):
  return render(request,'company.html')
  #return HttpResponse("THIS IS A PROJECT COMPANY PAGE")

def aboutus(request):
  return render(request,'aboutus.html')
  #return HttpResponse("THIS IS A PROJECT ABOUTUS PAGE")

def login(request):
  return render(request,'login.html')
  #return HttpResponse("THIS IS A PROJECT LOGIN PAGE")

def singup(request):
  return render(request,'singup.html')
  #return HttpResponse("THIS IS A PROJECT ABOUTUS PAGE")


def comsingup(request):
  if request.method == "POST":

    email = request.POST.get('email')
    password = request.POST.get('password')
    companyname = request.POST.get('companyname')
    tradelicense = request.POST.get('tradelicense')
    address = request.POST.get('address')
    phone = request.POST.get('phone')
    city = request.POST.get('city')

    comsingup = Comsingup(email=email,password=password,companyname=companyname,address=address,tradelicense=tradelicense,phone=phone,city=city)
    comsingup.save()
    messages.success(request, "Your Company Profile details updated.")




  return render(request,'comsingup.html')



def adminlogin(request):
  return HttpResponse("THIS IS A ADMIN LOGIN PAGE")

def comlogin(request):
  if request.method == "POST":
    username=request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:

      messages.success(request, "Username and Password Correct Login Successful")
       # A backend authenticated the credentials
      return redirect("/")

    else:
      # No backend authenticated the credentials
         return render(request,'comlogin.html')


    # email = request.POST.get('email')
    # password=request.POST.get('password')
    # comlogin=Comlogin(email=email,password=password)
    # comlogin.save()



  return render(request,template_name='comlogin.html')




def candidatelogin(request):

  if request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get('password')
    comlogin=Comlogin(email=email,password=password)
    comlogin.save()
  return render(request,template_name='candidatelogin.html')


def home(request):

  return render(request,'home.html')

def candidatesingup(request):
  if request.method == "POST":
    email = request.POST.get('email')
    password = request.POST.get('password')
    username = request.POST.get('username')
    education = request.POST.get('education')
    institution = request.POST.get('institution')
    phone = request.POST.get('phone')
    city = request.POST.get('city')
    file=request.POST.get('file')
    candidatesingup = Candidatesingup(email=email,password=password,username=username,institution=institution,education=education,phone=phone,city=city,file=file)
    candidatesingup.save()
    messages.success(request, "Your Candidate Profile details updated.")


  return render(request,'candidatesingup.html')