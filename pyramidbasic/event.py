# -*- coding: utf-8 -*-

from pyramid.events import (
    subscriber,
    ApplicationCreated,
    BeforeRender,
)

@subscriber(ApplicationCreated)
def setup_model(event):
    from .models import setup_model
    settings = event.app.registry.settings
    setup_model(settings)

@subscriber(BeforeRender)
def add_humanize(event):
    import humanize
    event['humanize'] = humanize
