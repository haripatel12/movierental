from django.forms import ModelForm
from .models import Customer,Movie

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first','last','phonenumber','email','address']

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['moviename','releasedate','genre','price','assigncustomer']