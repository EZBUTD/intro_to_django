from django import forms

class CommentForm(forms.Form):
	
	Identifier=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form', 'placeholder' : 'Identifier'}),initial=123456) #field that hold the unique key
	name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form', 'placeholder' : 'Name'}))
	comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form', 'placeholder' : 'Comment'}))