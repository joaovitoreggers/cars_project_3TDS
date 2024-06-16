from django import forms
from cars.models import Brand, Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1970:
            self.add_error('factory_year', 'O carro a ser cadastrado não pode ter um ano de fabricação anterior a 1970')
        return factory_year 