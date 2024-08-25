"""Configuration file for the Sphinx documentation builder.

This file only contains a selection of the most common options. For a full
list see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

# -- Path setup --------------------------------------------------------------
import os
import sys
from pathlib import Path
from typing import Any, Dict

from sphinx.application import Sphinx
from sphinx.locale import _
from datetime import datetime
from sphinx.util import logging

# from sphinx_syft_theme import __version__
__version__ = "0.0.0"

LOGGER = logging.getLogger("conf")

# Get the current year
current_year = datetime.now().year

sys.path.append(str(Path(".").resolve()))

# -- Project information -----------------------------------------------------

project = "Syft Theme"
copyright = f"{current_year}, Sphinx Syft Theme"
author = "Syft Theme Maintainer"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.graphviz",
    "sphinxext.rediraffe",
    "sphinx_design",
    "sphinx_copybutton",
    # "autoapi.extension",
    # custom extentions
    # "_extension.gallery_directive",
    # "_extension.component_directive",
    # For extension examples and demos
    "myst_parser",
    "ablog",
    "jupyter_sphinx",
    "sphinxcontrib.youtube",
    "nbsphinx",
    "numpydoc",
    "sphinx_togglebutton",
    "jupyterlite_sphinx",
    "sphinx_favicon",
    # "myst_nb",
    "sphinx_click.ext",
    "sphinx_comments",
    "sphinx_external_toc",
    # "sphinx_tabs.tabs",
    "sphinx_thebe",
    "sphinxcontrib.bibtex",
    "sphinxext.opengraph",
]

# -- MyST options ------------------------------------------------------------

# This allows us to use ::: to denote directives, useful for admonitions
# myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
]
myst_heading_anchors = 2
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}
myst_url_schemes = ["mailto", "http", "https"]

# Jupyter Notebooks configuration
nb_execution_mode = "force"
jupyterlite_config = "jupyterlite_config.json"

bibtex_bibfiles = ["references.bib"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints", ".tox"]

intersphinx_mapping = {"sphinx": ("https://www.sphinx-doc.org/en/master", None)}

# -- Sitemap -----------------------------------------------------------------

# ReadTheDocs has its own way of generating sitemaps, etc.
if not os.environ.get("READTHEDOCS"):
    extensions += ["sphinx_sitemap"]

    html_baseurl = os.environ.get("SITEMAP_URL_BASE", "http://127.0.0.1:8000/")
    sitemap_locales = [None]
    sitemap_url_scheme = "{link}"


# -- Internationalization ----------------------------------------------------

# specifying the natural language populates some key tags
language = "en"

# -- Ablog options -----------------------------------------------------------

blog_path = ""
blog_authors = {
    "jupyter": ("Jupyter", "https://jupyter.org"),
}


# -- sphinx_ext_graphviz options ---------------------------------------------

graphviz_output_format = "svg"
inheritance_graph_attrs = dict(
    rankdir="LR",
    fontsize=14,
    ratio="compress",
)

rediraffe_redirects = {
    # "contributing.md": "contributing/setup.md",
}

# Opengraph social cards
ogp_social_cards = {
    "image": "_static/images/logo.png",
}
ogp_site_url = "https://executablebooks.org/en/latest/"

# -- Options for autosummary/autodoc output ------------------------------------
autosummary_generate = True
autodoc_typehints = "description"
autodoc_member_order = "groupwise"
numpydoc_class_members_toctree = False

# -- sphinx_togglebutton options ---------------------------------------------
togglebutton_hint = str(_("Click to expand"))
togglebutton_hint_hide = str(_("Click to collapse"))

fontawesome_included = True

# -- favicon options ---------------------------------------------------------

# see https://sphinx-favicon.readthedocs.io for more information about the
# sphinx-favicon extension
favicons = [
    # generic icons compatible with most browsers
    "images/favicon/favicon-32x32.png",
    "images/favicon/favicon-16x16.png",
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
    # chrome specific
    "images/favicon/android-chrome-192x192.png",
    # apple icons
    {"rel": "apple-touch-icon", "href": "images/favicon/apple-touch-icon.png"},
    # msapplications
    {"name": "msapplication-TileColor", "content": "#459db9"},
    {"name": "theme-color", "content": "#ffffff"},
    {"name": "msapplication-TileImage", "content": "images/favicon/mstile-150x150.png"},
]

# -- Sphinx-copybutton options ---------------------------------------------
# Exclude copy button from appearing over notebook cell numbers by using :not()
# The default copybutton selector is `div.highlight pre`
# https://github.com/executablebooks/sphinx-copybutton/blob/master/sphinx_copybutton/__init__.py#L82
copybutton_selector = ":not(.prompt) > div.highlight pre"

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_syft_theme"
html_logo = "_static/images/logo-dark.svg"
html_favicon = "_static/images/favicon.ico"
html_sourcelink_suffix = ""
html_last_updated_fmt = ""  # to reveal the build date in the pages meta

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["css/*"]
html_js_files = ["js/*"]

html_sidebars = {
    # This ensures we test for custom sidebars
    "**": [
        "search-button-field.html",
        "sidebar-nav-bs",
    ],
    "standalone": [],
}

html_context = {
    "github_user": "callezenwaka",
    "github_repo": "syftbook",
    "github_version": "main",
    "doc_path": "docs",
}

# Theme config
todo_include_todos = True
external_toc_path = "_toc.yml"  # optional, default: _toc.yml
external_toc_exclude_missing = False  # optional, default: False

# Define the json_url for our version switcher.
json_url = "https://sphinx-syft-theme.readthedocs.io/en/latest/_static/switcher.json"

# # Define the version we use for matching in the version switcher.
# version_match = os.environ.get("READTHEDOCS_VERSION")
# release = sphinx_syft_theme.__version__
# # If READTHEDOCS_VERSION doesn't exist, we're not on RTD
# # If it is an integer, we're in a PR build and the version isn't correct.
# # If it's "latest" → change to "dev" (that's what we want the switcher to call it)
# if not version_match or version_match.isdigit() or version_match == "latest":
#     # For local development, infer the version to match from the package.
#     if "dev" in release or "rc" in release:
#         version_match = "dev"
#         # We want to keep the relative reference if we are in dev mode
#         # but we want the whole url if we are effectively in a released version
#         json_url = "_static/switcher.json"
#     else:
#         version_match = f"v{release}"
# elif version_match == "stable":
#     version_match = f"v{release}"

#
html_theme_options = {
    "analytics": {
        "plausiable__analytics_domain": "foo",
        "plausible__analytics_url": '<script defer="defer"> data-domain=toto src=http://.../script.js </script>,',
    },
    # "navbar_center": ["navbar-menu"],
    "header_links_before_dropdown": 4,
    "navbar_links": [
        {"name": "Documentation", "url": "index"},
        {"name": "Tools", "url": "tools/python"},
        {"name": "Syft", "url": "syft/syft"},
        {"name": "Contribute", "url": "contribute/contribute"},
    ],
    "external_links": [
        {
            "url": "https://syft.org",
            "name": "Syft",
        },
    ],
    "icon_links": [
        {
            "name": "Twitter",
            "url": "https://twitter.com/callezenwaka",
            "icon": "_static/images/icon/twitter.svg",
            "type": "local",
        },
        {
            "name": "GitHub",
            "url": "https://github.com/callezenwaka/sphinx-syft-theme",
            "icon": "_static/images/icon/github.svg",
            "type": "local",
        },
        {
            "name": "Slack",
            "url": "https://github.com/callezenwaka/sphinx-syft-theme",
            "icon": "_static/images/icon/slack.svg",
            "type": "local",
        },
    ],
    "text_links": [
        {
            "name": "Join on slack for #support",
            "url": "https://slack.com/",
            "icon": "_static/images/icon/slack.svg",
            "type": "local",
        },
    ],
    "logo": {
        "text": "Syft Theme",
        "image_light": "_static/images/logo-light.svg",
    },
    "use_edit_page_button": True,
    "show_sidebar_on_root_doc": True,  # or False
    "home_page_in_toc": True,
    "show_toc_level": 3,
    "show_nav_level": 3,
    "navbar_align": "content",  # [left, content, right] For testing that the navbar items align properly
    "announcement": f"⚠️This is an experimental release <a href='https://pypi.org/project/sphinx-syft-theme/{__version__}/' target='_blank'>sphinx-syft-theme</a> ⚠️",
    "show_version_warning_banner": True,
    # "navbar_center": ["version-switcher", "navbar-nav"],
    # "navbar_start": ["navbar-logo"],
    # "navbar_end": ["theme-switcher", "navbar-icon-links"],
    # "navbar_persistent": ["search-button"],
    # "primary_sidebar_end": ["custom-template", "sidebar-ethical-ads"],
    # "article_footer_items": ["test", "test"],
    # "content_footer_items": ["test", "test"],
    # "footer_start": ["copyright"],
    # "footer_center": ["sphinx-version"],
    # "secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    "secondary_sidebar_items": {
        "**": ["page-toc", "edit-this-page", "sourcelink"],
        # "**/*": ["page-toc", "edit-this-page", "sourcelink"],
        # "examples/no-sidebar": [],
        "standalone": [],
    },
    # "switcher": {
    #     "json_url": json_url,
    #     "version_match": version_match,
    # },
    # "back_to_top_button": False,
    "custom_shortcode_to_image": {
        "|:persona:|": "/_static/images/persona.png",
    },
}

# -- application setup -------------------------------------------------------


def setup_to_main(
    app: Sphinx, pagename: str, templatename: str, context, doctree
) -> None:
    """Add a function that jinja can access for returning an "edit this page" link pointing to `main`."""

    def to_main(link: str) -> str:
        """Transform "edit on github" links and make sure they always point to the main branch.

        Args:
            link: the link to the github edit interface

        Returns:
            the link to the tip of the main branch for the same file
        """
        links = link.split("/")
        idx = links.index("edit")
        return "/".join(links[: idx + 1]) + "/main/" + "/".join(links[idx + 2 :])

    context["to_main"] = to_main


def setup(app: Sphinx) -> Dict[str, Any]:
    """Add custom configuration to sphinx app.

    Args:
        app: the Sphinx application
    Returns:
        the 2 parallel parameters set to ``True``.
    """
    app.connect("html-page-context", setup_to_main)

    return {
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
