from django.http import HttpResponse
from django.shortcuts import redirect
import time


def unaunthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *args, **kwargs)

    
    return wrapper_func


def allowed_user(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request, *args, **kwargs):

            group= None
            if request.user.groups.exists():
                group= request.user.groups.all()[0].name
            
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('no esta permitido entrar a esta pagina')

                
                
        return wrapper_func
    return decorators
