import magic
from django import forms
from django.core.exceptions import ValidationError

class CSVForm(forms.Form):
    file=forms.FileField()

    def clean_file(self):
        file = self.cleaned_data.get("file", False)
        filetype = magic.from_buffer(file.read(2048))
        print(filetype)
        if "CSV text" and "ASCII text" not in filetype:
            raise ValidationError("That file is not CSV.")
        return file