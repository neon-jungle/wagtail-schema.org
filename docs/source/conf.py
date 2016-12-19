#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wagtailschemaorg._version import version_bits

# -- General configuration ------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

source_suffix = '.rst'
master_doc = 'index'

project = 'Wagtail Schema.org JSON-LD tags'
copyright = '2016, Takeflight'
author = 'Takeflight'

# The short X.Y version.
version = '.'.join(map(str, version_bits[:2]))
# The full version, including alpha/beta/rc tags.
release = '.'.join(map(str, version_bits))

pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

htmlhelp_basename = 'WagtailSchemaOrg'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

latex_documents = [
    (master_doc, 'WagtailSchemaOrg.tex', 'Wagtail Schema.org JSON-LD tags documentation',
     'Takeflight', 'manual'),
]


# -- Options for manual page output ---------------------------------------

man_pages = [
    (master_doc, 'wagtailschemaorg', 'Wagtail Schema.org JSON-LD tags Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'WagtailSchemaorg', 'Wagtail Schema.org JSON-LD tags Documentation',
     author, 'WagtailSchemaorg', 'Schema.org JSON-LD tags for Wagtail sites',
     'Miscellaneous'),
]


# -- Options for intersphinx ----------------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.5/', None),
    'django': ('https://docs.djangoproject.com/en/dev/', 'https://docs.djangoproject.com/en/dev/_objects/'),
}
