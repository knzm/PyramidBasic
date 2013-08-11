# -*- coding: utf-8 -*-

from pyramid_layout.layout import layout_config

from js.jquery import jquery
from js.modernizr import modernizr
from js.bootstrap import bootstrap


@layout_config(template='pyramidbasic:templates/layout.jinja2')
class MyLayout(object):
    page_title = "Pyramid Basic App"

    def __init__(self, context, request):
        self.context = context
        self.request = request

        jquery.need()
        modernizr.need()
        bootstrap.need()

    def deform_static_url(self, link):
        return self.request.static_url('deform:static/' + link)
