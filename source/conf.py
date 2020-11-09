# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Ess_Documentation'
copyright = '2020, AdamZh0u'
author = 'AdamZh0u'

# The full version, including alpha/beta/rc tags
release = '0.1.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

master_doc = "index"

source_suffix = ['.rst', '.md']

language = None
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
pygments_style = 'sphinx'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'cloud'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['../_static']
html_js_files = [
    'js/baidutongji.js', ]

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}

# --Latex ----------------------------------------------------------------
latex_elements = {  # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',  # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '12pt', 'classoptions': ',oneside', 'babel': '',  # 必须
    'inputenc': '',  # 必须
    'utf8extra': '',  # 必须
    # Additional stuff for the LaTeX preamble.
    'preamble': r"""
\usepackage{xeCJK}
\usepackage{indentfirst}
\setlength{\parindent}{2em}
\setCJKmainfont{WenQuanYi Micro Hei}
\setCJKmonofont[Scale=0.9]{WenQuanYi Micro Hei Mono}
\setCJKfamilyfont{song}{WenQuanYi Micro Hei}
\setCJKfamilyfont{sf}{WenQuanYi Micro Hei}
\XeTeXlinebreaklocale "zh"
\XeTeXlinebreakskip = 0pt plus 1pt
      """}

# +extensions++++++++++++++++++++++++++++++++++++++++++++++

_exts = "../exts"
sys.path.append(os.path.abspath(_exts))

extensions = ['recommonmark',
              'chinese_search',
              'sphinx_markdown_tables',
              'sphinxemoji.sphinxemoji',
              'sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.intersphinx',
              'sphinx.ext.todo',
              'sphinx.ext.coverage',
              'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages',
              # Auto-generate section labels.
              'sphinx.ext.autosectionlabel',
              ]
autosectionlabel_prefix_document = True
