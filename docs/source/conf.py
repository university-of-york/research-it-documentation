# Configuration file for the Sphinx documentation builder.

import sys
import os

# -- Project information

project = 'Viking Documentation'
copyright = '2023, The University of York'
author = 'The University of York'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    # 'logo_only': True,
    'display_version': False,
    # 'style_nav_header_background': '#144835',  # dark green
    'style_nav_header_background': '#A6A091',  # tan
}

html_favicon = 'assets/img/favicon.ico'
html_logo = 'assets/img/logo_white_sm.png'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'

# include replacements
sys.path.append(os.path.join(os.path.dirname(__file__), '.'))
from replacements import *
