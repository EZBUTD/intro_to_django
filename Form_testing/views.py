from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm
from django import forms

class TestForm(forms.Form): #linking to a class outside views.py caused me issues, I'm not sure why.
    Identifier=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form', 'placeholder' : 'Identifier'}))
    name = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'class': 'form', 'placeholder' : 'Name'}))
    comments = forms.CharField(widget=forms.Textarea(attrs={'class': 'form', 'placeholder' : 'Comment'}))

# Create your views here.
def index1(request):
    comments = Comment.objects.order_by('-date_added')

    context ={'comments': comments}

    return render(request, 'C:/Users/chener/Documents/intro_to_django/Form_testing/templates/form/index.html', context) #replace this with your location of the html file

def sign1(request): #this handles the POST request and stores the data in a table.
    if request.method =='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            try:
                ID_test=Comment.objects.filter(Identifier=request.POST['Identifier']).values('comments')[0]['comments'] #test if existing comment is there. If it isn't it will return an IndexError.
                update_comment=Comment.objects.filter(Identifier=request.POST['Identifier']).update(comments=request.POST['comments'], name=request.POST['name']) #if it is, then update it
            except IndexError:#if existing comment does not exist, create a new row. If the user wants a separate row for each comment, remove the try portion of this code.
                new_comment=Comment(Identifier=request.POST['Identifier'], name=request.POST['name'], comments=request.POST['comments'])
                new_comment.save()
            return redirect('index')
    else:
        form=CommentForm()



    context ={'form' : form}
    return render(request, 'C:/Users/chener/Documents/intro_to_django/Form_testing/templates/form/sign.html',context) #replace this with your location of the html file

def sign_detail21(request, ID_value): #this handles filling in the form with an existing comment or leaving the form blank
    try:
        comments = Comment.objects.filter(Identifier=ID_value).values('comments')[0]['comments'] #queries last comment made for given ID
    except IndexError: #error for when there is no existing comment to pull, pass in blank value instead
        comments = ''
    if request.method =='POST':
        form=TestForm(request.POST)    
    else:
        form=TestForm(initial=dict(Identifier=ID_value,comments=comments))

    context ={'form' : form, 'ID_value' : ID_value} 
    return render(request, 'C:/Users/chener/Documents/intro_to_django/Form_testing/templates/form/sign.html', context) #replace this with your location of the html file