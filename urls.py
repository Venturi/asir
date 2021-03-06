# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from aldryn_django.utils import i18n_patterns

import django.contrib.auth
import aldryn_addons.urls

urlpatterns = [
    # add your own patterns here
    url('^', include('django.contrib.auth.urls')),
] + aldryn_addons.urls.patterns() + i18n_patterns(
    # add your own i18n patterns here
    *aldryn_addons.urls.i18n_patterns()  # MUST be the last entry!
)
