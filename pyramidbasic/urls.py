# -*- coding: utf-8 -*-

def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('top', '/')
    config.add_route('login', '/account/login')
    config.add_route('logout', '/account/logout')
