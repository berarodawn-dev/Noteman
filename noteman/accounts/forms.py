from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model
from .models import Note, Task


class SignupForm(UserCreationForm):
    """
    A user signup form that handles the parsing of fields to make a new user
    - username
    - password1
    - password2

    Only contains class meta unless you want to add in other fields

    model = get_user_model() -> retunr user model

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = get_user_model()  # retrives the current active user model in the project
        fields = ["username", "password1", "password2"]

class LoginForm(forms.Form):
    '''
    A login form that parses the input for logins
    
    - username
    - password

    No Meta because this is a normal form inheriting form forms.Form. It doesnt make a
    new object or anything else. Just provides fields and validates them for login
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    username = forms.CharField(max_length=20, required=True)
    password = forms.CharField(max_length=150, required=True, widget=forms.PasswordInput)



class NoteCreationForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = 'form-control'


    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea, max_length=1000)

    class Meta:
        model = Note
        fields = ["title", "content"]


class TaskCreationForm(forms.ModelForm):

    def __init__(self,*args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs["class"] = 'form-control'
                        
    class Meta:
        model = Task
        fields = ["content"]
