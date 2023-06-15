
from django.forms import models, forms

from catalog.models import Product

BLOCKED_WORDS = {"казино", "криптовалюта", "крипта", "биржа",
                 "дешево", "бесплатно", "обман", "полиция", "радар", "дёшево"}
class ProductForm(models.ModelForm):
    class Meta:
        model = Product
        exclude = ("creation_date", "modification_date")

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
