from django.contrib import admin

# Register your models here.
from myadmin.models import Notice#(modelname

admin.site.site_header = 'Notice Hub Web-App'
admin.site.index_title = 'Admin Panel'

class NoticeAdmin(admin.ModelAdmin):
	list_display = ['id','subject','description','created_at','updated_at']

admin.site.register(Notice, NoticeAdmin)
