from django.http import HttpResponseForbidden

def rol_requerido(rol):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.rol == rol:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("No autorizado")
        return wrapper
    return decorator