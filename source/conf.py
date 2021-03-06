# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Autocall'
copyright = '2020, TEL4VN'
author = 'TEL4VN'

# The full version, including alpha/beta/rc tags
release = 'v1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# latex_engine = 'xelatex'

html_static_path = ['_static']

html_css_files = ['css/custom.css']


# The master toctree document.


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'vi'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'p-greenblue'
import os
# from PSphinxTheme import utils
from PSphinxTheme.utils import set_psphinxtheme

'PSphinxTheme.ext.psphinx_admonitions',

'PSphinxTheme.ext.escaped_samp_literals',

'PSphinxTheme.ext.index_styling',

'PSphinxTheme.ext.sidebarlogo_perpag',

'PSphinxTheme.ext.relbar_links',

'PSphinxTheme.ext.table_styling',


html_theme_path, html_theme, needs_sphinx = set_psphinxtheme(html_theme)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# html_sidebars = {
#     '**':  ['globaltoc.html'],
# }




# [optional] overwrite some of the default options listed above...
# https://pythonhosted.org/PSphinxTheme/main_theme.html#structure

html_theme_options = { 
					# "lighter_decor": True,
					# "sidebarwidth": 300,
					"sidebar_localtoc_title": "Content",
					"bodyfont": "arial"}

html_logo = os.path.join('_static', 'pitel-autocall.png')

html_favicon = os.path.join('_static', 'pitel-autocall.png')

# The api document: extension: relbar_links
relbar_links_doc = [
   ('toc', 'index'),
   ('user-guide', 'user-guide'),
   ('api', 'api/index')
]

# common_sidebars = ['quicklinks.html', 'sourcelink.html', 'searchbox.html']
common_sidebars = ['quicklinks.html']

html_sidebars = {
   '**': ['localtoc.html', 'relations.html'] + common_sidebars,
   'py-modindex': common_sidebars,
   'genindex': common_sidebars,
   'search': common_sidebars,
}