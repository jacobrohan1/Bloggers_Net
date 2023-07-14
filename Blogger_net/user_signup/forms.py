from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.shortcuts import render, redirect

class CustomUserCreationForm(UserCreationForm):
    # Add additional fields or customizations to your form
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # redirect to home page
    
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})