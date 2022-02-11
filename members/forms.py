from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from blog.models import Profile


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = 'form-control'
        self.fields["first_name"].widget.attrs['class'] = 'form-control'
        self.fields["last_name"].widget.attrs['class'] = 'form-control'
        self.fields["email"].widget.attrs['class'] = 'form-control'
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].widget.attrs['class'] = 'form-control'


class ProfilePageForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'insta_url', 'twitter_url')
        
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            #'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'insta_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditProfilePageForm(forms.ModelForm):
    class Meta: 
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'insta_url', 'twitter_url')
        
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            #'profile_pic': forms.TextInput(attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'insta_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = 'form-control'
        self.fields["first_name"].widget.attrs['class'] = 'form-control'
        self.fields["last_name"].widget.attrs['class'] = 'form-control'
        self.fields["email"].widget.attrs['class'] = 'form-control'
    

class PasswordChangingForm(PasswordChangeForm):
    #old_password = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))
    #new_password1 = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))
    #new_password2 = forms.CharField(widget=forms.PasswordInput(attrs = {'class': 'form-control', 'type':'password'}))


    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')

    def __init__(self, *args, **kwargs):
        super(PasswordChangingForm, self).__init__(*args, **kwargs)
        self.fields["old_password"].widget.attrs['class'] = 'form-control'
        self.fields["new_password1"].widget.attrs['class'] = 'form-control'
        self.fields["new_password2"].widget.attrs['class'] = 'form-control'
