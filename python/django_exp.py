# flake8: noqa

# django
import django




# django settings
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE = 5 * 60  # 5 minutes

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'testdb',
        'USER': 'testuser',
        'PASSWORD': 'testpassword',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}










# forms

# make all form fields not required
def __init__(self, *args, **kwargs):
    super(TestForm, self).__init__(*args, **kwargs)

    for field in self.fields:
        self.field.required = False









# models
import models

from django.db import models


# all users where pk < 5
User.objects.filter(pk__lt=5)
User.objects.filter(pk__lte=6)

# all users starting with joh
User.objects.filter(username__icontains='joh')

# users in
User.objects.filter(pk__in=[1, 4, 7])

# sort by date
User.objects.order_by('date')
User.objects.order_by('-date')


# print raw sql query
print(Mymodel.objects.all().query)


# show all sql queries
from django.db import connection
connection.queries




# get model to avoid circular imports
from django.db.models import get_model
get_model('<app>', '<model>')

# manually select databse
Book.objects.using('test_db').all()

# queryset database
book._state.db











# views

# custom 404 - add this to views.py
from django.shortcuts import render_to_response
from django.template import RequestContext


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response



# admin
from django.contrib import admin

class ProposalSectionReviewerAdmin(AuditAdmin):
    list_display = ('conference_reviewer', 'proposal_section') + AuditAdmin.list_display
    list_filter = ['proposal_section']

    def get_queryset(self, request):
        qs = super(ProposalSectionReviewerAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs









# templates

from django.template import loader
print(loader.get_template('home.html'))

# show all templates
from django.template.loaders.app_directories import app_template_dirs
template_files = []
for template_dir in (settings.TEMPLATE_DIRS + app_template_dirs):
    for dir, dirnames, filenames in os.walk(template_dir):
        for filename in filenames:
        template_files.append(os.path.join(dir, filename))


# django>1.9
from django.conf import settings
from django.template.loaders.app_directories import get_app_template_dirs
import os

template_dir_list = []
for each in get_app_template_dirs('templates'):
    if settings.ROOT_DIR in each:
        template_dir_list.append(each)


template_list = []
for each in (template_dir_list + settings.TEMPLATES[0]['DIRS']):
    for dir, dirnames, filenames in os.walk(each):
        for filename in filenames:
            template_list.append(os.path.join(each, filename))














# urls

# all URL patterns excluding namespaces
from django.core.urlresolvers import get_resolver
get_resolver(None).reverse_dict.keys()

# get view
reverse('/')
# lazy version of reverse
reverse_lazy('/')
reverse('foo:bar')
# with query params
url = '{}?{}'.format(reverse('foo:bar'), 'q=foo')



# redirect
(r'^one/$', redirect_to, {'url': '/another/'}),
(r'^one/$', RedirectView.as_view(url='/another/')),







# admin
"{% url 'admin:index' %}"













# mail
import django.core.mail

from django.core.mail import mail_admins
subject = 'foo'
message = 'bar'
mail_admins(subject, message)














# call management command from script
from django.core.management import call_command

call_command('flush', verbosity=0, interactive=False)


# management commands

# add cli argument
def add_arguments(self, parser):
    parser.add_argument('my_int_argument', type=int)

def handle(self, *args, **options):
    my_int_argument = options['my_int_argument']


# django-autofixture

# create 30 instances of model
# python manage.py loadtestdata proposals.Proposal:30








# django i18n

# templates

# db



from django.utils import autoreload

def do_something(*args, **kwargs):
    # management command logic


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout('This command auto reloads. No need to restart...')
        autoreload.main(do_something, args=None, kwargs=None)




# translations
