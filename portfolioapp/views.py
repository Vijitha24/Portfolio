
from django.shortcuts import render, redirect
from .models import Portfolio,About, Project, WorkExperience, Education, Certification,Skill


def index(request):
    project = Project.objects.all()
    about = About.objects.all()
    portfolio = Portfolio.objects.all()
    education = Education.objects.all()
    experience = WorkExperience.objects.all()
    certificate = Certification.objects.all()
    skill = Skill.objects.all()

    return render(request,"index.html",{
        'portfolios': portfolio,
        'projects' : project,
        'abouts'    : about,
        'educations' : education,
        'experiences' : experience,
        'certificates' :certificate,
        'skills'      :skill

    })