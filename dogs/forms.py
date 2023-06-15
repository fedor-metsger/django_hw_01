from datetime import datetime, timedelta, date
from datetime import timedelta
from django.forms import models, forms

from dogs.models import Dog, Breed, Ancestor

class DogForm(models.ModelForm):
    class Meta:
        model = Dog
        exclude = ("breed",)

    def __init__(self, *args, **kwargs):
        self.breed_id = kwargs["breed_id"]
        del kwargs["breed_id"]
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def save(self, *args, **kwargs):
        self.instance.breed = Breed.objects.get(pk=self.breed_id)
        return super().save(*args, **kwargs)

    def clean_birthdate(self):
        cleaned_data = self.cleaned_data["birthdate"]

        if cleaned_data < date.today() - timedelta(days=100 * 365):
            raise forms.ValidationError("Возраст не должен быть больше 100 лет.")
        return cleaned_data

class AncestorForm(models.ModelForm):
    class Meta:
        model = Ancestor
        exclude = ("dog",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"