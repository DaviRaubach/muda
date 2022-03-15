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

#
import os
import sys
# import muda

sys.path.insert(0, os.path.abspath('../../'))
sys.setrecursionlimit(2000)



# -- Project information -----------------------------------------------------

project = 'Muda'
copyright = '2022, Davi Raubach Tuchtenhagen'
author = 'Davi Raubach'

# The full version, including alpha/beta/rc tags
release = '0.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxnotes.lilypond',
    # 'abjad.ext.sphinx',
    'rinoh.frontend.sphinx',
    'sphinx.ext.autodoc',
    # 'sphinx.ext.graphviz',
    "sphinx.ext.doctest",
    # "sphinx.ext.intersphinx",
    # "sphinx.ext.mathjax",
    # "sphinx.ext.viewcode",
    'sphinxcontrib.pdfembed',

]

doctest_global_setup = '''
import abjad
import muda
from abjadext import rmakers
'''

# graphviz_dot_args = ["-s32"]
# graphviz_output_format = "svg"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "furo"
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt,'
}

lilypond_fontsize = [6, -3]
lilypond_preamble = ''
lilypond_fontsize = [10, -3]
lilypond_command = 'lilypond'
lilypond_args = []
lilypond_score_format = "png"

