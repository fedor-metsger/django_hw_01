
from django.forms import models, forms, BaseInlineFormSet
from django.core.exceptions import ValidationError
from catalog.models import Product, Version

BLOCKED_WORDS = {"казино", "криптовалюта", "крипта", "биржа",
                 "дешево", "бесплатно", "обман", "полиция", "радар", "дёшево"}

# class VersionFormFormSet(BaseInlineFormSet):
#     def clean(self):
#         curr = False
#         for f in self.forms:
#             if "current" in f.cleaned_data and f.cleaned_data["current"]:
#                 if not curr:
#                     curr = True
#                 else:
#                     raise forms.ValidationError("Может быть только одна активная версия продукта!")
#         return super().clean()

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

    # current_count = 0

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs["class"] = "form-control"
        self.fields["number"].widget.attrs["class"] = "form-control"

    # def clean_current(self):
    #     cleaned_data = self.cleaned_data["current"]
    #     if self.cleaned_data["current"]:
    #         self.current_count += 1
    #     if self.current_count > 1:
    #         raise ValidationError("Может быть только одна активная версия продукта!")
    #
    #     return cleaned_data