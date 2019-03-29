"""from django.core.exceptions import ValidationError
def validate_file_size(value):
    filesize = value.size

    if filesize > 307200:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value
"""
from django.core.exceptions import ValidationError
def validate_file_size():
    file = open("Task1.csv")
    numline = len(file.readlines())
    print (numline)
    if numline < 300:
        raise ValidationError("The maximum file length that can be uploaded is more than 300 rows")
    else:
        print("file is verify")