
from django.forms import models, forms, BaseInlineFormSet
from django.core.exceptions import ValidationError

from catalog.models import Product, Version
from users.models import User

BLOCKED_WORDS = {"казино", "криптовалюта", "крипта", "биржа",
                 "дешево", "бесплатно", "обман", "полиция", "радар", "дёшево"}

class ProductForm(models.ModelForm):
    class Meta:
        model = Product
        exclude = ("creation_date", "modification_date", "owner")

    def __init__(self, *args, **kwargs):
        self.owner_id = None
        if "owner_id" in kwargs:
            self.owner_id = kwargs["owner_id"]
            del kwargs["owner_id"]
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control"

    def save(self, *args, **kwargs):
        if self.owner_id:
            self.instance.owner = User.objects.get(pk=self.owner_id)
        return super().save(*args, **kwargs)

    def clean_name(self):
        cleaned_data = self.cleaned_data["name"]

        for w in BLOCKED_WORDS:
            if w in cleaned_data.lower():
                raise ValidationError("Нельзя вводить запрещённые продукты!")
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]

        for w in BLOCKED_WORDS:
            if w in cleaned_data.lower():
                raise ValidationError("Нельзя вводить запрещённые продукты!")
        return cleaned_data

class VersionForm(models.ModelForm):
    class Meta:
        model = Version
        exclude = ("product",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["number"].widget.attrs["class"] = "form-control"
