from django.contrib import admin
from django.urls import path,include
from home_page import views
from .views import authView
urlpatterns = [

  path("",views.index,name="home_page"),
  path("comsingup/",authView,name="authView"),
  path("accounts/", include("django.contrib.auth.urls")),
  path("home",views.home,name="home"),
  path("jobs",views.jobs,name="about"),
  path("candidates",views.candidates,name="candidates"),
  path("company",views.company,name="company"),
  path("aboutus",views.aboutus,name="aboutus"),
  path("login",views.login,name="login"),
  path("singup",views.singup,name="singup"),
  path("adminlogin",views.adminlogin,name="adminlogin"),
  path("comsingup",views.comsingup,name="comsingup"),
  path("comlogin",views.comlogin,name="comlogin"),
  path("candidatelogin",views.candidatelogin,name="condidatelogin"),
  path("candidatesingup",views.candidatesingup,name="candidatesingup")
]