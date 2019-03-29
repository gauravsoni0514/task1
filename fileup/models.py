from django.db import models
#from fileup.validators import validate_file_size
#from django.core.exceptions import ValidationError
class Inputfile(models.Model):
    uname=models.CharField(max_length=200)
    ufile = models.FileField(upload_to='csv/', null=True, verbose_name="")
    class Meta:
        db_table="inputfile"


    def __str__(self):
        #return self.uname + ": " + str(self.ufile)
        return self.uname
"""def validate_file_size(self):
        # ufile=csv.DictReader(request.FILES['csv'])
        file = open("ufile")
        numline = len(file.readlines())
        print(numline)
        if numline < 300:
            raise ValidationError("The maximum file length that can be uploaded is more than 300 rows")
        else:
            print("file is verify")"""
#validators=[validate_file_size]
