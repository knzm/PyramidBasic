# -*- coding: utf-8 -*-

import colander as c
import deform.widget as w
from pyramid.view import view_config
from pyramid import security
from pyramid.httpexceptions import HTTPFound
from pyramid_deform import FormView

from pyramidbasic.security import login


class LoginSchema(c.Schema):
    user_name = c.SchemaNode(c.String(), title=u"ユーザ名")
    password = c.SchemaNode(c.String(), title=u"パスワード",
                            widget=w.PasswordWidget())


@view_config(route_name="login", renderer="login.jinja2")
class LoginForm(FormView):
    schema = LoginSchema()
    buttons = ('login',)

    def login_success(self, values):
        user_name = values['user_name']
        password = values['password']
        userid, headers = login(self.request, user_name, password)
        if userid is None:
            self.request.session.flash(u"ユーザ名とパスワードが一致しません")
            return

        response = HTTPFound(self.request.route_url('top'))
        response.headerlist.extend(headers)
        return response


@view_config(route_name='logout')
def logout_view(request):
    headers = security.forget(request)
    response = HTTPFound(request.route_url('top'))
    response.headerlist.extend(headers)
    request.session.flash(u"ログアウトしました")
    return response
