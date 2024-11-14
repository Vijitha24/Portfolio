from django.contrib import admin

# Register your models here.
from .models import Portfolio,About,Education,WorkExperience,Skill,Project,Certification

admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Project)
admin.site.register(Certification)
