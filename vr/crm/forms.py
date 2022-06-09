from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Ваше Имя'}))
    phone = forms.CharField(max_length=200,
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите телефон'}))
