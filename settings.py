# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'aldryn-devsync',
    'aldryn-bootstrap3',
    'aldryn-common',
    'aldryn-disqus',
    'aldryn-emailsettings',
    'aldryn-events',
    'aldryn-faq',
    'aldryn-forms',
    'aldryn-jobs',
    'aldryn-newsblog',
    'aldryn-people',
    'aldryn-style',
    # </INSTALLED_ADDONS>
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([
    # add you project specific apps here
])

TEMPLATE_CONTEXT_PROCESSORS.extend([
    # add your template context processors here
    TEMPLATE_DIRS, ALLOWED_INCLUDE_ROOTS, TEMPLATE_CONTEXT_PROCESSORS, TEMPLATE_LOADERS
])

MIDDLEWARE_CLASSES.extend([
    # add your own middlewares here
])

#LDAP

import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

AUTHENTICATION_BACKENDS = (
	'django_auth_ldap.backend.LDAPBackend',
	'django.contrib.auth.backends.ModelBackend',
)

AUTH_LDAP_SERVER_URI = "ldap://192.168.2.144:10389"

AUTH_LDAP_BIND_DN = "uid=asir,ou=users,dc=example,dc=com"
AUTH_LDAP_BIND_PASSWORD = "asir"
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=example,dc=com",
			ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
)
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=Groups,dc=example,dc=com",
    ldap.SCOPE_SUBTREE, "(objectClass=PosixGroup)"
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType()

