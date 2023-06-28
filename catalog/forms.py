
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

    def __init__(self, *args, owner_id=None, moderator=None, owner=None, **kwargs):
        self.owner_id = owner_id
        self.moderator = moderator
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if moderator:
                if not owner and field_name not in {"description", "category"}:
                    field.disabled = True
            if field_name != "published":
                field.widget.attrs["class"] = "form-control"
            else:
                field.disabled = not moderator

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
