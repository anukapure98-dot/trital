from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm
from .models import Member
from django.contrib.auth.decorators import login_required
from functools import wraps
from django.http import HttpResponse


def register_member(request):

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return render(request, 'success.html')

    else:
        form = MemberForm()

    return render(request, 'register.html', {'form': form})

def basic_auth_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        auth = request.META.get('HTTP_AUTHORIZATION')

        if auth:
            import base64

            try:
                method, credentials = auth.split(' ')
                if method.lower() == 'basic':
                    username, password = base64.b64decode(
                        credentials
                    ).decode().split(':')

                    if username == 'admin' and password == 'supertrital':
                        return view_func(request, *args, **kwargs)
            except Exception:
                pass

        response = HttpResponse("Authentication Required", status=401)
        response['WWW-Authenticate'] = 'Basic realm="Members Area"'
        return response

    return wrapper

@basic_auth_required
def member_list(request):
    members = Member.objects.all().order_by('id')
    return render(request, 'member_list.html', {'members': members})

def print_member(request, pk):

    member = get_object_or_404(Member, id=pk)

    return render(request, 'print_form.html', {
        'member': member
    })