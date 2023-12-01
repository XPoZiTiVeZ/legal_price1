from django.shortcuts import render, redirect
from rest_framework.response import Response
from django.http import HttpResponse
from django.contrib import auth
from django.views.decorators.csrf import csrf_protect, csrf_exempt

def web_page(request):
    # if not request.user.is_authenticated:
    #     return redirect('/login')
    return render(request, 'pages/untitled.html')
@csrf_exempt
def login(request):
    args = {}
    if request.POST:
    #args.update(csrf(request))
        email = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=email, password=password)
        if user != None:
            print('login success')
            auth.login(request, user)
            return HttpResponse('success', status=200)
        else:
            print('bad login or password')
            args['error'] = 'Неверный логин или пароль. Повторите попытку или нажмите на ссылку &quot;Забыли пароль?&quot;, чтобы сбросить его.'
            return HttpResponse('error', status=403)
    else:
        return render(request, "pages/index.html", args)
def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
