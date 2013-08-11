# -*- coding: utf-8 -*-

from pyramid.view import view_config

@view_config(route_name='top', request_method='GET', renderer='top.jinja2')
def top_view(request):
    return {}
