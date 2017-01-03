Project Makefile Open for Business
==================================

.. post:: 2016/11/23
    :category: Plone, Python

**Makefile for Python Web Development & Related Projects**

A while back I was asked to speak to the Configuration Management Working Group of DC:

.. image:: /images/project-makefile-tweet.png
    :align: center
    :class: img-thumbnail
    :target: https://twitter.com/CMWorkingGrp/status/773228143939293185

From that moment on, it was on: an excuse to finish and talk about the ``Makefile`` I'd been dragging around *formerly since January* and informerly much longer.

Finishing the Makefile
----------------------

I started writing slides on the `impressive slides.com <http://slides.com/aclark/project-makefile>`_ then I realized I had to finished the Makefile to finish the slides. This mostly involved deciding on target names and testing target execution.

Finishing the Slides
--------------------

As I mentioned above, slides.com is *very* nice. I had hoped to be able to build the slides myself with reveal.js, but in lieu of JavaScript skills I settled on using the slides.com editor. Later I exported and converted them to PDF with pandoc, which was not as nice (through no fault of pandoc, I'm sure; I just wish I could get a better PDF copy from the slides.com HTML export.)

Closed for Business
-------------------

For month after month as I continued to tweak, the project-makefile repository README contained the following::

    **DO NOT USE THIS**

    At some point I started using a ``Makefile`` in my Python projects. This repository
    contains that ``Makefile``.

    **shrug**

Open for Business
-----------------

Now it contains this::

    Installation
    ------------

    ::

        curl -O https://raw.githubusercontent.com/aclark4life/project-makefile/master/Makefile


    Usage
    -----

    ::

        Usage: make [TARGET]
        Available targets:

            - ablog
            - ablog-build
            - ablog-clean
            - ablog-init
            - ablog-install
            - ablog-serve
            - co
            - commit
            - commit-auto
            - commit-edit
            - django
            - django-clean
            - django-clean-migrations
            - django-init
            - django-install
            - django-migrate
            - django-migrations
            - django-serve
            - django-shell
            - django-static
            - django-su
            - django-test
            - django-yapf
            - git-checkout-remotes
            - git-commit
            - git-commit-auto
            - git-commit-auto-push
            - git-commit-edit
            - git-push
            - grunt
            - grunt-file
            - grunt-init
            - grunt-install
            - grunt-serve
            - h
            - he
            - heroku
            - heroku-debug-off
            - heroku-debug-on
            - heroku-init
            - heroku-push
            - heroku-remote
            - heroku-shell
            - heroku-web-off
            - heroku-web-on
            - install
            - lint
            - npm
            - npm-init
            - npm-install
            - package
            - package-check-manifest
            - package-init
            - package-lint
            - package-pyroma
            - package-readme
            - package-release
            - package-release-test
            - package-test
            - pdf
            - plone
            - plone-heroku
            - plone-init
            - plone-install
            - plone-serve
            - push
            - python-clean
            - python-flake
            - python-freeze
            - python-install
            - python-lint
            - python-serve
            - python-virtualenv
            - python-wc
            - python-yapf
            - release
            - release-test
            - review
            - serve
            - sphinx
            - sphinx-build
            - sphinx-clean
            - sphinx-init
            - sphinx-install
            - sphinx-serve
            - test
            - vagrant
            - vagrant-clean
            - vagrant-down
            - vagrant-init
            - vagrant-up
            - vagrant-update
            - vm

    - Check out the `slides <http://slides.com/aclark/project-makefile>`_ for more information.

Now I invite everyone to use and contribute!

- https://github.com/aclark4life/project-makefile

|
