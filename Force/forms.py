# Import the necessary forms module from Django
from django import forms

# Create a custom form named PredictionForm, which inherits from the Django's base Form class

# Define choices for the 'RM' field, these will be displayed as options in a dropdown menu
class PredictionForm(forms.Form):
    RM_choices = (
        ('300', '300'),
        ('400', '400'),
        ('500', '500'),
        ('600', '600'),
        ('700', '700'),
        ('800', '800'),
        ('1000', '1000'),
        ('1200', '1200'),
        ('1300', '1300'),
        ('1400', '1400'),
        ('1500', '1500'),
        ('1600', '1600'),
        ('1700', '1700'),
        ('1900', '1900'),
        ('2000', '2000'),
        )

    # Create the fields for the form, each field corresponds to an input element in the HTML form

    # Field for 'Largeur' (Width) with a Float value (decimal number) as input
    Largeur = forms.FloatField(label='Largeur (mm)')

    # Field for 'RM' (RESISTANCE MAXIMARE) with choices displayed in a dropdown menu
    RM = forms.ChoiceField(choices=RM_choices, label='Résistence Max (MPA)')

    # Field for 'Thickness' with a Float value (decimal number) as input, limited to a range between 0.0 and 100.0
    Thickness = forms.FloatField(label='Epaisseur (mm)', min_value=0.0, max_value=100.0)

class upload_model(forms.Form):
    name = forms.CharField(max_length=100)
    model_file = forms.FileField()
    scaler_file = forms.FileField()

