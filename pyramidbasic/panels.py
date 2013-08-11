# -*- coding: utf-8 -*-

from pyramid_layout.panel import panel_config
from pyramid import security


@panel_config('flash', renderer='templates/panel/flash.jinja2')
def flash_panel(context, request, queue=''):
    return {
        'messages': request.session.pop_flash(queue),
        }

@panel_config('login_menuitem', renderer="templates/panel/login_menuitem.jinja2")
def login_menuitem_panel(context, request):
    return {
        'userid': security.authenticated_userid(request),
        'login_url': request.route_url('login'),
        'logout_url': request.route_url('logout'),
        }
