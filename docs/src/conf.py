# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Add the local lib to path if desired
# import sys
# sys.path.insert(0, os.path.abspath('/Users/ctlee/gamer/gamer/buildpy35/lib/'))

import os
import pygamer

_on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# -- Project information -----------------------------------------------------

project = 'GAMer'
copyright = '2019, Christopher T. Lee'
author = 'Christopher T. Lee'

version = '2.0.2'
release = 'v2.0.2-dev-13-g72cfedb.dirty'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx_issues',
    'nbsphinx',
    'jupyter_sphinx.embed_widgets',
]

# Github repo
issues_github_path = 'ctlee/gamer'

if(True):
    extensions.extend(['breathe', 'exhale'])

##############################
# Breathe Settings
##############################
breathe_projects = { "gamer_project": "/Users/ctlee/gamer/gamer/docs/src/_doxyoutput/xml" }
breathe_default_project = "gamer_project"

##############################
# Exhale Settings
##############################

doxystdin = \
"""
INPUT = /Users/ctlee/gamer/gamer/include
OPTIMIZE_OUTPUT_FOR_C  = YES
EXTRACT_ALL            = YES
"""
# ENABLED_SECTIONS       = detail

exhale_args = {
    "containmentFolder":     "/Users/ctlee/gamer/gamer/docs/src/_cppapi",
    "rootFileName":          "root.rst",
    "rootFileTitle":         "C++ API Reference",
    "doxygenStripFromPath":  "/Users/ctlee/gamer/gamer",
    # "pageLevelConfigMeta":   ":github_url: https://github.com/ctlee/gamer",
    "createTreeView":        True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin":    doxystdin,
}


##############################
# Autosummary Settings
##############################

autosummary_generate = True
# autodoc_default_flags = ['members', 'inherited-members']

# try to exclude deprecated
# def skip_deprecated(app, what, name, obj, skip, options):
#     if hasattr(obj, "func_dict") and "__deprecated__" in obj.func_dict:
#         print("skipping " + name)
#         return True
#     return skip or False

# def setup(app):
#     app.connect('autodoc-skip-member', skip_deprecated)
#     try:
#         from sphinx.ext.autosummary import Autosummary
#         from sphinx.ext.autosummary import get_documenter
#         from docutils.parsers.rst import directives
#         from sphinx.util.inspect import safe_getattr
#         import re

#         class AutoAutoSummary(Autosummary):

#             option_spec = {
#                 'methods': directives.unchanged,
#                 'attributes': directives.unchanged
#             }

#             required_arguments = 1

#             @staticmethod
#             def get_members(obj, typ, include_public=None):
#                 if not include_public:
#                     include_public = []
#                 items = []
#                 for name in dir(obj):
#                     try:
#                         documenter = get_documenter(app, safe_getattr(obj, name), obj)
#                     except AttributeError:
#                         continue
#                     if documenter.objtype == typ:
#                         items.append(name)
#                 public = [x for x in items if x in include_public or not x.startswith('_')]
#                 return public, items

#             def run(self):
#                 clazz = self.arguments[0]
#                 try:
#                     (module_name, class_name) = clazz.rsplit('.', 1)
#                     m = __import__(module_name, globals(), locals(), [class_name])
#                     c = getattr(m, class_name)
#                     if 'methods' in self.options:
#                         _, methods = self.get_members(c, 'method', ['__init__'])

#                         self.content = ["~%s.%s" % (clazz, method) for method in methods if not method.startswith('_')]
#                     if 'attributes' in self.options:
#                         _, attribs = self.get_members(c, 'attribute')
#                         self.content = ["~%s.%s" % (clazz, attrib) for attrib in attribs if not attrib.startswith('_')]
#                 finally:
#                     return super(AutoAutoSummary, self).run()

#         app.add_directive('autoautosummary', AutoAutoSummary)
#     except BaseException as e:
#         raise e


##############################
# Napoleon Settings
##############################
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = True
napoleon_use_param = True
napoleon_use_rtype = True

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
show_authors = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['/Users/ctlee/gamer/gamer/docs/src/_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_templates', '**.ipynb_checkpoints']



##############################
# HTML Output Settings
##############################

# Try to load sphinx_rtd_theme otherwise fallback on default
try:
    import sphinx_rtd_theme
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
    html_theme = 'sphinx_rtd_theme'
except ImportError:
    html_theme = 'default'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['/Users/ctlee/gamer/gamer/docs/src/_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }

##############################
# Intersphinx Settings
##############################

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'https://docs.python.org/': None}
