from django.db import models


class NIWETable(models.Model):
    id = models.IntegerField(primary_key=True)
    sendermail = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    receivermail = models.CharField(max_length=50)
    ccmail = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    remarks = models.CharField(max_length=200)
    duedate = models.DateField()

    class Meta:
        db_table = "niwetable2"
# Create your models here.
