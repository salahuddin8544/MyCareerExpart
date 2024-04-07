from django.contrib import admin
from .models import Country, HighestDegree, Language, Specialization, SectorExperience, JobType, Job, Company, CvTemplate
# Register your models here.
admin.site.register(Country)
admin.site.register(HighestDegree)
admin.site.register(Language)
admin.site.register(Specialization)
admin.site.register(SectorExperience)
admin.site.register(Job)
admin.site.register(JobType)
admin.site.register(Company)
admin.site.register(CvTemplate)