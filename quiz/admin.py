from django.contrib import admin

from .models import Options, Question, Question_Set
# Register your models here.

admin.site.register(Options)
admin.site.register(Question)
admin.site.register(Question_Set)