from django.db import models

# Create your models here.
class Notice(models.Model):
      subject = models.CharField(max_length=200)
      description = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
 #by deafault tablename is foldername_modelname
 #rename the tablename
  #class Meta:
 	#db_table = 'notice'
