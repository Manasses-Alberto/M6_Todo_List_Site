from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/auth/login/')
def home(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request,
                      'login.html',
                      {'error': False,
                        'email_error': False,
                        'password_error': False,
                        'message': None,
                        'email': '',
                        'password': ''
                        })

    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.filter(email=email).first()
        if not username:
            print('Username error')
            return render(request,
                          'login.html',
                          {'error': True,
                            'email_error': True,
                            'password_error': False,
                            'message': 'Email inválido. Tente novamente!',
                            'email': '',
                            'password': password
                            })

        else:
            user_auth = authenticate(request, username=username.username, password=password)
            try:
                auth_login(request, user_auth)
            
            except AttributeError:
                return render(request,
                              'login.html',
                              {'error': True,
                               'email_error': False,
                               'password_error': True,
                               'message': 'Senha inválida. Tente novamente!',
                               'email': email,
                               'password': ''
                               })

            else:
                return redirect('home')

def register(request):
    if request.method == 'GET':
        return render(request,
                      'register.html',
                      {'error': False,
                        'username_error': False,
                        'email_error': False,
                        'password_error': False,
                        'message': None,
                        'username': '',
                        'email': '',
                        'password': '',
                        'password_conf': ''
                        })
    
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_conf = request.POST['password-confirmation']
        old_username = User.objects.filter(username=username).first()
        old_email = User.objects.filter(email=email).first()
        if old_username:
            print('Username error')
            return render(request,
                          'register.html',
                          {'error': True,
                            'username_error': True,
                            'email_error': False,
                            'password_error': False,
                            'message': 'Este nome de usuário já existe. Tente novamente!',
                            'username': '',
                            'email': email,
                            'password': password,
                            'password_conf': password_conf
                            })

        elif old_email:
            print('Email error')
            return render(request,
                          'register.html',
                          {'error': True,
                            'email_error': True,
                            'username_error': False,
                            'password_error': False,
                            'message': 'Este email já existe. Tente novamente!',
                            'username': username,
                            'email': '',
                            'password': password,
                            'password_conf': password_conf
                            })

        elif password != password_conf:
            print('Password error')
            return render(request,
                          'register.html',
                          {'error': True,
                            'password_error': True,
                            'email_error': False,
                            'password_error': False,
                            'message': 'As suas senhas estão diferentes. Tente novamente!',
                            'username': username,
                            'email': email,
                            'password': '',
                            'password_conf': ''
                            })

        else:
            new_user = User.objects.create_user(username=username, email=email, password=password)
            new_user.save()
            user_auth = authenticate(request, username=username, password=password)
            auth_login(request, user_auth)
            return redirect('home')
