# -*- coding: utf-8 -*-

# Alex Clark's Blog build configuration file, created by
# `ablog start` on Wed Oct 21 06:05:23 2015.
#
# Note that not all possible configuration values are present in this file.
# All configuration values have a default; values that are commented out
# serve to show the default.

import ablog

# -- General ABlog Options ----------------------------------------------------

# A path relative to the configuration directory for blog archive pages.
# blog_path = 'blog'

# The “title” for the blog, used in acthive pages.  Default is ``'Blog'``.
blog_title = u'Alex Clark\'s Blog'

# Base URL for the website, required for generating feeds.
# e.g. blog_baseurl = "http://example.com/"
blog_baseurl = u'True'

# Choose to archive only post titles. Archiving only titles can speed
# up project building.
# blog_archive_titles = False

# -- Blog Authors, Languages, and Locations -----------------------------------

# A dictionary of author names mapping to author full display names and
# links. Dictionary keys are what should be used in ``post`` directive
# to refer to the author.  Default is ``{}``.
blog_authors = {'Alex Clark': ('Alex Clark', None), }

# A dictionary of language code names mapping to full display names and
# links of these languages. Similar to :confval:`blog_authors`, dictionary
# keys should be used in ``post`` directive to refer to the locations.
# Default is ``{}``.
# blog_languages = {
#    'en': ('English', None),
# }

# A dictionary of location names mapping to full display names and
# links of these locations. Similar to :confval:`blog_authors`, dictionary
# keys should be used in ``post`` directive to refer to the locations.
# Default is ``{}``.
# blog_locations = {
#    'Earth': ('The Blue Planet', 'http://en.wikipedia.org/wiki/Earth),
# }

# -- Blog Post Related --------------------------------------------------------

# post_date_format = '%b %d, %Y'

# Number of paragraphs (default is ``1``) that will be displayed as an excerpt
# from the post. Setting this ``0`` will result in displaying no post excerpt
# in archive pages.  This option can be set on a per post basis using
# post_auto_excerpt = 1

# Index of the image that will be displayed in the excerpt of the post.
# Default is ``0``, meaning no image.  Setting this to ``1`` will include
# the first image, when available, to the excerpt.  This option can be set
# on a per post basis using :rst:dir:`post` directive option ``image``.
# post_auto_image = 0

# Number of seconds (default is ``5``) that a redirect page waits before
# refreshing the page to redirect to the post.
# post_redirect_refresh = 5

# When ``True``, post title and excerpt is always taken from the section that
# contains the :rst:dir:`post` directive, instead of the document. This is the
# behavior when :rst:dir:`post` is used multiple times in a document. Default
# is ``False``.
# post_always_section = False

# -- ABlog Sidebars -------------------------------------------------------

# There are seven sidebars you can include in your HTML output.
# postcard.html provides information regarding the current post.
# recentposts.html lists most recent five posts. Others provide
# a link to a archive pages generated for each tag, category, and year.
# In addition, there are authors.html, languages.html, and locations.html
# sidebars that link to author and location archive pages.
html_sidebars = {
    '**': [
        'postcard.html',
        'recentposts.html',
        'categories.html',
        'archives.html',
        'searchbox.html',
    ],
}

# -- Blog Feed Options --------------------------------------------------------

# Turn feeds by setting :confval:`blog_baseurl` configuration variable.
# Choose to create feeds per author, location, tag, category, and year,
# default is ``False``.
# blog_feed_archives = True

# Choose to display full text in blog feeds, default is ``False``.
blog_feed_fulltext = True

# Blog feed subtitle, default is ``None``.
# blog_feed_subtitle = None

# Choose to feed only post titles, default is ``False``.
# blog_feed_titles = False

# Specify number of recent posts to include in feeds, default is ``None``
# for all posts.
# blog_feed_length = 1

# -- Font-Awesome Options -----------------------------------------------------

# ABlog templates will use of Font Awesome icons if one of the following
# is ``True``

# Link to `Font Awesome`_ at `Bootstrap CDN`_ and use icons in sidebars
# and post footers.  Default: ``False``
fontawesome_link_cdn = True

# Sphinx_ theme already links to `Font Awesome`_.  Default: ``False``
# fontawesome_included = False

# Alternatively, you can provide the path to `Font Awesome`_ :file:`.css`
# with the configuration option: fontawesome_css_file
# Path to `Font Awesome`_ :file:`.css` (default is ``None``) that will
# be linked to in HTML output by ABlog.
# fontawesome_css_file = None

# -- Disqus Integration -------------------------------------------------------

# You can enable Disqus_ by setting ``disqus_shortname`` variable.
# Disqus_ short name for the blog.
# disqus_shortname = None

# Choose to disqus pages that are not posts, default is ``False``.
# disqus_pages = False

# Choose to disqus posts that are drafts (without a published date),
# default is ``False``.
# disqus_drafts = False

# -- Sphinx Options -----------------------------------------------------------

# If your project needs a minimal Sphinx version, state it here.
needs_sphinx = '1.2'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'alabaster',
    'ablog',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', ablog.get_html_templates_path()]

# The suffix(es) of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Alex Clark\'s Blog'
copyright = u'2015, Alex Clark'
author = u'Alex Clark'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = ''
# The full version, including alpha/beta/rc tags.
release = ''

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['lib']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {
#    'github_button': False,
# }

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = [alabaster.get_path()]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "Alex Clark's Blog"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "Alex Clark's Blog"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'AlexClarksBlogdoc'

import sphinx_bootstrap_theme
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# (Optional) Logo. Should be small enough to fit the navbar (ideally 24x24).
# Path should be relative to the ``_static`` files directory.
# html_logo = "my_logo.png"

# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_theme_options = {
    # Navigation bar title. (Default: ``project`` value)
    # 'navbar_title': "Demo",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Pages",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        ("RSS", "/blog/atom.xml"),
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': " ",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,

    # Include hidden TOCs in Site navbar?
    #
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    #
    # Values: "true" (default) or "false"
    'globaltoc_includehidden': "true",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",

    # Fix navigation bar to top of page?
    # Values: "true" (default) or "false"
    'navbar_fixed_top': "true",

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "footer",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "amelia" or "cosmo".
    # 'bootswatch_theme': "cerulean",
    # 'bootswatch_theme': "cosmo",
    # 'bootswatch_theme': "cyborg",
    # 'bootswatch_theme': "darkly",
    # 'bootswatch_theme': "flatly",
    # 'bootswatch_theme': "journal",
    # 'bootswatch_theme': "lumen",
    # 'bootswatch_theme': "paper",
    'bootswatch_theme': "readable",
    # 'bootswatch_theme': "sandstone",
    # 'bootswatch_theme': "simplex",
    # 'bootswatch_theme': "slate",
    # 'bootswatch_theme': "spacelab",
    # 'bootswatch_theme': "superhero",
    # 'bootswatch_theme': "united",
    # 'bootswatch_theme': "yeti",

    # Choose Bootstrap version.
    # Values: "3" (default) or "2" (in quotes)
    'bootstrap_version': "3",
}

disqus_shortname = 'aclark-blog'
blog_baseurl = 'http://blog.aclark.net'
