from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Employee
from myapp.models import Resume

def Home(request):
    if request.method=="POST":
        id=request.POST.get('emid')
        nm=request.POST.get('nm')
        pst=request.POST.get('pst')
        email=request.POST.get('email')
        joind=request.POST.get('jd')
        emp=Employee(Emp_Id=id,Emp_Name=nm,Emp_Post=pst,Emp_Email=email,Emp_JoinD=joind)
        emp.save()
    return render(request,"Homepage.html")

def About(request):
    return render(request,"About.html")

def Service(request):
    return render(request,"Service.html")

def Setting(request):
    return render(request,"Setting.html")

def secondpage(request):
    return render(request,"secondpage.html")

def Contact(request):
    return render(request,'Contact.html')

# def Resume(request):
#     return render(request,"Resume.html",{"Name":"Rahul Singh","About":"I am dedicated to improving my skills through hands-on learning and development work.Proficient in desktop enviornment.Adept at using Reactjs, JavaScript and other programming language to produce clean code.Well-orgnized and passionate to learning new technology and i am able to work in a team with problem solving skills in creating and designing a website.","Intern":"Intern At Brillica Service","Project1":"Lamonk and Brillica Service Static Website Using HTML,CSS.","Project2":"Meal finder app using API.","Project3":"Coffee Shop Responsive Website using HTML,CSS,JS.","Project4":"Education Website using ReactJs.","Skill1":"HTML","Skill2":"CSS","Skill3":"JAVASCRIPT","Skill4":"BOOTSTRAP","Skill5":"REACT.JS","Skill6":"Core PYTHON","Skill7":"DJANGO","edu1":"BA,DAV PG College Dehradun(HNB University)  06/2020-present","edu2":"Inter College GIC Kulsari(Chamoli)  2016-2018","add1":"Ability to communicate with cross functional team.","add2":"Intrested and passionate to learn professional skill.","add3":"Good Communication skill.","add4":"Fast learner.","hob1":"Reading Biographical Books.","hob2":"Watching Biographical Movie.","hob3":"Lisening Music.","int1":"Passionate to leran Machine learning and AI.","int2":"Photography.","int3":"Playing Cricket.","cou1":"Full Stack Development 2022-Present","cou2":"Englidh Speaking Course 08/2022-09/2022","lan1":"Hindi","lan2":"English"})