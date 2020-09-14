from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Details

#admin.site.register(Details)

# Define the admin class
class DetailsAdmin(admin.ModelAdmin):
    list_display = ('Name', 'age', 'gender', 'mobile', 'w_mobile', 'stage', 'occupation', 'skills', 'comments', 'created_date', 'resume')
    #list_display = ('Name', 'age', 'gender', 'mobile')

#Register the admin class with the associated model
admin.site.register(Details,DetailsAdmin)

