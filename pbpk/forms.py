from django.contrib.auth.models import User
from django import forms
from pbpk.models import Models, Drug



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class DrugForm(forms.ModelForm):
    class Meta:
        model=Drug
        exclude = ('drugname',)
        widgets = {
            'drugname': forms.TextInput,
        }

class ModelForm(forms.ModelForm):

    class Meta:
        model = Models
        exclude = ('username','drugs',)
        error_css_class = 'error'


        widgets = {
            'username': forms.TextInput,
            'modelname': forms.TextInput,
        }

    def clean(self):
        cleaned_data = super(ModelForm, self).clean()
        blood_volume_fraction = cleaned_data.get("blood_volume_fraction")
        lung_flow_factor = cleaned_data.get("lung_flow_factor")
        lung_volume_fraction= cleaned_data.get("lung_volume_fraction")
        blood_lung_fraction = cleaned_data.get("blood_lung_fraction")

        if blood_volume_fraction and lung_flow_factor and lung_volume_fraction and blood_lung_fraction:
            # Only do something if both fields are valid so far.
            if ((blood_volume_fraction == "0.0") & ((lung_flow_factor=="0.0") | (lung_volume_fraction=="0.0") | (blood_lung_fraction == "0.0") )) :

                raise forms.ValidationError("Cannot be created model without blood and lung.")
            elif (blood_volume_fraction == "0.0") :
                msg="Cannot be created model without blood!!"
                self.add_error(None, msg)
                raise forms.ValidationError("Cannot be created model without blood.")
        return cleaned_data
