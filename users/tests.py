from django.test import TestCase
from django.contrib.auth.forms import UserCreation Form

def register(request):
	form = UserCreationForm()
	return render(request, 'users/register.html', {'form': form})