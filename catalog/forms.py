
from django.forms import models, forms

from catalog.models import Product, Version

BLOCKED_WORDS = {"казино", "криптовалюта", "крипта", "биржа",
                 "дешево", "бесплатно", "обман", "полиция", "радар", "дёшево"}
class ProductForm(models.ModelForm):
    class Meta:
        model = Product
        exclude = ("creation_date", "modification_date")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        for w in BLOCKED_WORDS:
            if w in cleaned_data.lower():
                raise forms.ValidationError("Нельзя вводить запрещённые продукты!")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        for w in BLOCKED_WORDS:
            if w in cleaned_data.lower():
                raise forms.ValidationError("Нельзя вводить запрещённые продукты!")
        return cleaned_data

class VersionForm(models.ModelForm):
    class Meta:
        model = Version
        exclude = ("product",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["number"].widget.attrs["class"] = "form-control"
