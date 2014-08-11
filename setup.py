#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from distutils.core import Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        from django.conf import settings
        settings.configure(
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            INSTALLED_APPS=('lobbying',)
        )
        from django.core.management import call_command
        call_command('test', 'lobbying')


setup(
    name='django-calaccess-lobbying-activity',
    version='0.2',
    packages=[
        'lobbying',
        'lobbying.management',
        'lobbying.management.commands',
	'lobbying.utils',
    ],
    include_package_data=True,
    license='MIT License',  # example license
    description='A simple Django app browse California lobbying activity data from Cal-Access.',
    url='https://github.com/california-civic-data-coalition',
    author='California Civic Data Coalition',
    author_email='awilliams@cironline.org',
    install_requires=(
       # 'django-calaccess-parser>=0.2',
        'django>=1.6',
        'csvkit==0.6.1',
        'python-dateutil==2.1',
        'MySQL-python==1.2.5',
        'argparse==1.2.1',
        'requests==2.2.1',
        'progressbar>=2.2',
        'hurry.filesize==0.9',
        'pypandoc==0.8.0',
    ),
    cmdclass={'test': TestCommand}
)
