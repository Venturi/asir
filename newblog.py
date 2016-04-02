# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

import cms.api
from cms.models import Page
import aldryn_newsblog

from django.conf import settings
from django_auth_ldap.backend import LDAPBackend

class Command(BaseCommand):
	help = 'Crea la página web para el usuario proporcionado'

	def add_arguments(self, parser):
		parser.add_argument('usuario', nargs='+', type=str)

	def handle(self, *args, **options):
		usuario = options['usuario'][0]

		ldap = LDAPBackend()

		user = ldap.populate_user(usuario)

		user_config = aldryn_newsblog.models.NewsBlogConfig(namespace=usuario,app_title=usuario.capitalize())
		user_config.save_base()
		user_config.create_translation(language_code='en')

		parent_menu = Page.objects.filter(title_set__title = 'Alumnos')[0]

		page = cms.api.create_page(user.username, 'fullwidth.html', 'en', apphook='NewsBlogApp', apphook_namespace=user_config.namespace, parent=parent_menu, in_navigation=True,published=True)

		placeholder = page.placeholders.get(slot='feature')
		plugin = cms.api.add_plugin(placeholder, 'StylePlugin','en',class_name='feature-visual-narrow')

		user_assigned = cms.api.assign_user_to_page(page,user,grant_all=True)

		page.publish(language='en')

		self.stdout.write('Se ha creado el blog para el usuario "%s"' % usuario)
