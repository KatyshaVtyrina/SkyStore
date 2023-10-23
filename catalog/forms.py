from django import forms

from catalog.models import Product, Version


class StyleForMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleForMixin, forms.ModelForm):

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price')

    def clean_title(self):
        clean_title = self.cleaned_data['title']
        for word in self.forbidden_words:
            if word in clean_title.lower():
                raise forms.ValidationError(f'Название не может содержать слово "{word}"')
        return clean_title

    def clean_description(self):
        clean_description = self.cleaned_data['description']
        for word in self.forbidden_words:
            if word in clean_description.lower():
                raise forms.ValidationError(f'Описание не может содержать слово "{word}"')
        return clean_description


class VersionForm(StyleForMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
