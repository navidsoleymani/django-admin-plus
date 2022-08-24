from setuptools import setup, find_packages

setup(
    name='django_admin_plus',
    version='3.1',
    license='MIT',
    author='Navid Soleymani',
    author_email='navidsoleymani@ymail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/navidsoleymani/django-admin-plus',
    keywords='Python Django-admin-plus',
    install_requires=[
        'typer',
        'colorama',
        'shellingham',
        'pytest',
        'Django',
        'djangorestframework',
        'markdown',
        'django-filter',
    ],
)
