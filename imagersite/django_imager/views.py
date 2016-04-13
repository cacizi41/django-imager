# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView


# def home_page(request, *args, **kwargs):
    # kwargstring = argstring = ""
    # if args:
    #     argstring = "args: {}".foramt(", ".join(args))
    # if kwargs:
    #     kwargstring = "kwargs:\n{}".foramt(
    #         "".join("\t{}:{}\n".format(key, val) for key, val in kwargs.items())
    # return HttpResponse("Hello!")

def home_page(request, *args, **kwargs):
    foo = 'garbanzo beans'
    # body = template.render{{foo:}}
    return HttpResponse(foo)

class ClassView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, num=0, name='balloons'):
        return {'num': num, 'name': name}
