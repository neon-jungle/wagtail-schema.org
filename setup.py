#!/usr/bin/env python
"""
Install wagtail-schema.org using setuptools
"""

from setuptools import find_packages, setup

with open('README.rst', 'r') as f:
    readme = f.read()

with open('wagtailschemaorg/_version.py', 'r') as f:
    version = '0.0.0'
    exec(f.read())

setup(
    name='wagtail-schema.org',
    version=version,
    description="Add Schema.org JSON-LD to your website",
    long_description=readme,
    author='Tim Heap',
    author_email='tim@takeflight.com.au',
    url='https://github.com/takeflight/wagtail-schema.org',

    install_requires=[
        'wagtail>=5.2',
    ],
    extras_require={
        'testing': ['jinja2>=2.10,<3.0', 'markupsafe==2.0.1']
    },
    zip_safe=False,
    license='BSD License',

    packages=find_packages(),

    include_package_data=True,
    package_data={},

    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Django',
        'Framework :: Django :: 3',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4',
        'Framework :: Django :: 4.2',
        'Framework :: Django :: 5',
        'Framework :: Django :: 5.0',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 5',
        'Framework :: Wagtail :: 6',
        'License :: OSI Approved :: BSD License',
    ],
)
