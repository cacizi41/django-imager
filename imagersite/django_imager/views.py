# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from registration.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm



# def home_page(request, *args, **kwargs):
    # kwargstring = argstring = ""
    # if args:
    #     argstring = "args: {}".foramt(", ".join(args))
    # if kwargs:
    #     kwargstring = "kwargs:\n{}".foramt(
    #         "".join("\t{}:{}\n".format(key, val) for key, val in kwargs.items())
    # return HttpResponse("Hello!")

def home_page(request):
    sign_up_form = RegistrationForm()
    log_in_form = AuthenticationForm()
    return render(request, 'home.html', context={
        'signup': sign_up_form,
        'login': log_in_form
    })






# def log_in(request):
#     username = request.POST['username']
#     password = request.POST['password']
#     user = authenticate(username=username, password=password)
#     if user is not None:
#         if user.is_active:
#             login(request, user)
#             # Redirect to a success page.
#         else:
#             # Return a 'disabled account' error message
#             ...
#     else:
#         # Return an 'invalid login' error message.