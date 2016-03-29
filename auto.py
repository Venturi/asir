import cms.api
import aldryn_newsblog

from django.conf import settings
from django_auth_ldap.backend import LDAPBackend

ldap = LDAPBackend()

user = ldap.populate_user('venturi')

user_config = aldryn_newsblog.models.NewsBlogConfig(namespace='venturi',app_title='Venturi')
user_config.save_base()
user_config.create_translation(language_code='en')

parent_menu = Page.objects.filter(title_set__title = 'Alumnos')[0]

page = cms.api.create_page(user.username, 'fullwidth.html', 'en', apphook='NewsBlogApp', apphook_namespace=user_config.namespace, parent=parent_menu in_navigation=True,published=True)

placeholder = page.placeholders.get(slot='feature')
plugin = cms.api.add_plugin(placeholder, 'StylePlugin','en',class_name='feature-visual-narrow')

#user = User.objects.filter(username='venturi')

user_assigned = cms.api.assign_user_to_page(page,user,grant_all=True)

page.publish(language='en')
