from django.contrib import admin
from .models import Choices,Question,Form



admin.site.register(Choices)
admin.site.register(Question)
admin.site.register(Form)