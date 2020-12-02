#https://stackoverflow.com/questions/3648421/only-accept-a-certain-file-type-in-filefield-server-side/43540603
import os
from django.core.exceptions import ValidationError
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('File must be PDF')