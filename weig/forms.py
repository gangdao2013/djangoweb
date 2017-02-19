from django import forms


class AddForm(forms.Form):
    a = forms.IntegerField(label='', error_messages={'required': '加数1'})
    b = forms.IntegerField(label='', error_messages={'required': '加数2'})
