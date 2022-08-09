from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
	"""Rejstracja nowego użytkownika"""
	if request.method != 'POST':
		#Wyświetlenie pustego formularza rejstracji użytkownika
		form = UserCreationForm()
	else:
		#Przetworzenie wypełnionego formularza
		form = UserCreationForm(data=request.POST)
		if form.is_valid():
			new_user = form.save()
			#Zalogowanie użytkownika i przekierowanie na homepage
			login(request, new_user)
			return redirect('learning_logs:index')
	#Wyświetlenie pustego formularza
	context = {'form': form}
	return render(request, 'registration/register.html', context)
