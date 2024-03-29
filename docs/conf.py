# global configuration for every documentation added at the end

import os, sys, datetime
import sphinx-rtd-theme

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.abspath(dir_path + '/_ext'))
now = datetime.datetime.now()

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

# General information about the project.
copyright = str(now.year) + ' Laduga'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'latest'
# The full version, including alpha/beta/rc tags.
release = version

# RTD theme options

html_theme = "sphinx_rtd_theme"

html_theme_options = {}

main_doc = 'contents'

# Disable click behavior for images
html_scaled_image_link = False

# relative path to subdirectories
html_logo = "../_shared_assets/static/logo-white.png"

# substitutions go here
##rst_epilog =  '.. |version| replace:: %s' % version

# building the versions list
##version_start = 19		# THIS IS THE SUPPORTED VERSION NUMBER
##version_stable = 21		# INCREASE THIS NUMBER TO THE LATEST STABLE VERSION NUMBER
##def generateVersionsDocs(current_docs):
##	versions_doc = []
##	for v in range(version_start, version_stable + 1):
##		url = 'https://docs.nextcloud.com/server/%s/%s' % (str(v), current_docs)
##		versions_doc.append(tuple((v, url)))
##	versions_doc.append(tuple(('stable', 'https://docs.nextcloud.com/server/%s/%s' % ('stable', current_docs))))
##	versions_doc.append(tuple(('latest', 'https://docs.nextcloud.com/server/%s/%s' % ('latest', current_docs))))
##	return versions_doc
	
##if version.isdigit():
##	github_branch = 'stable%s' % version
##else:
##	github_branch = 'main'

##html_context = {
##	'current_version': version,
##	'READTHEDOCS': True,
##	'extra_css_files': ['_static/custom.css'],

##	# force github plugin
##	'display_github': True,
##	'github_user': 'Pradis',
##	'github_repo': 'documentation',
	# If current version is an int, use the stablexxx branches, otherwise, edit on main
##	'theme_vcs_pageview_mode': 'edit/%s/' % github_branch, # to be completed by each individual conf.py
##}

##edit_on_github_project = 'Pradis/documentation'
##edit_on_github_branch = 'main'

html_static_path = ['/all_index/_static']
