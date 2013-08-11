# -*- coding: utf-8 -*-

from pyramid.authorization import ACLAuthorizationPolicy
from pyramid_who.whov2 import WhoV2AuthenticationPolicy


def login(request, user_name, password):
    from repoze.who.api import get_api
    who_api = get_api(request.environ)

    credentials = {
        'login': user_name,
        'password': password,
        }
    return who_api.login(credentials)


def groupfinder(identity, request):
    return []


def includeme(config):
    identifier_id = "auth_tkt"
    config_file = config.registry.settings.get('who.config_file')
    authentication_policy = WhoV2AuthenticationPolicy(
        config_file, identifier_id, callback=groupfinder)
    authorization_policy = ACLAuthorizationPolicy()
    config.set_authentication_policy(authentication_policy)
    config.set_authorization_policy(authorization_policy)
