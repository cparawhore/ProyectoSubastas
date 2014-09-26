from django import forms
from models import cloud_users
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
	username = forms.CharField(label="Nombre de Usuario",widget=forms.TextInput())
	email = forms.EmailField(label="Correo Electronico",widget=forms.TextInput())
	password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("Nombre de usuario ya existe")

	def clean_email(self):
		email = self.cleaned_data['email']
		try:
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email
		raise forms.ValidationError('Email ya registrado')

	def clean_password_two(self):
		password = self.cleaned_data['password_one']
		password_two = self.cleaned_data['password_two']
		if password == password_two:
			pass
		else:
			raise forms.ValidationError('Las Passwords no coinciden')

class ArticuloForm(forms.ModelForm):
	class Meta:
		model = cloud_users
	def clean_autor(self):
		diccionario_limpio = self.cleaned_data
		autor = diccionario_limpio.get('autor')
		if len(autor) < 3:
			raise forms.ValidationError("El autor debe contener mas de 3 caracteres")
		return autor

	def clean_titulo(self):
		diccionario_limpio = self.cleaned_data
		titulo = diccionario_limpio.get('titulo')

		if len(titulo)>50:
			raise forms.ValidationError("El titulo debe ser menor a 50 aracteres")
		return titulo

	def clean_texto(self):
		diccionario_limpio = self.cleaned_data
		texto = diccionario_limpio.get('texto')

		if len(texto) > 400:
			raise forms.ValidationError("El texto no debe estar vacio")

		return texto

	def clean_fecha(self):
		diccionario_limpio = self.cleaned_data
		fecha_articulo = diccionario_limpio.get('fecha')
		fecha_actual = timezone.now()

		if fecha_actual > fecha_articulo:
			raise forms.ValidationError("La fecha no debe ser mayor al dia de hoy")
		return fecha_articulo
