from django.shortcuts import render_to_response
from django.views.generic import CreateView
from store.models import cloud_users
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse_lazy
from store.forms import RegisterForm
from captcha.fields import CaptchaField
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

class RegistrarUsuario(CreateView):
	template_name = 'signup.html'
	model = cloud_users
	success_url = reverse_lazy('signup')

	def post(self,request,*args,**kwargs):
		cloudUser = cloud_users()
		cloudUser.cloud_user = request.POST['cloud_user']
		cloudUser.enc_pass = request.POST['enc_pass']
		cloudUser.ste_acc = request.POST['ste_acc']
		cloudUser.ste_acc_trd = request.POST['ste_acc_trd']
		cloudUser.save()
		return render_to_response('mensaje.html')

def iniciar_sesion(request):
	if not request.user.is_anonymous():
		return HttpResponseRedirect('../')
	if request.method == "POST":
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			username = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username = username, password = clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('../')
				else:
					return HttpResponseRedirect('../')
			else:
				return HttpResponseRedirect('/error')
	else:
		formulario = AuthenticationForm()

	return render_to_response('login.html',{'formulario': formulario}, context_instance=RequestContext(request))


def home(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

#def login(request):
#	return render_to_response('login.html', context_instance=RequestContext(request))

#def signup(request):
#	return render_to_response('signup.html', context_instance=RequestContext(request))

def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save()
			return render_to_response('thanks_register.html',context_instance=RequestContext(request))
		else:
			ctx = {'form':form}
			return render_to_response('signup.html',ctx,context_instance=RequestContext(request))
	ctx = {'form':form}
	return render_to_response('signup.html',ctx,context_instance=RequestContext(request))