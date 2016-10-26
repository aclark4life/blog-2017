Getting Excited About Plone as Eggs
===================================

.. post:: 2008/12/15
    :category: Buildout, Plone, Python

**Updated for 4.x**

I'm really excited about this because it greatly simplifies the development and deployment story for `Plone`_. For example you can now create a Plone ``buildout.cfg`` file like this:

::

    [buildout]
    extends = http://dist.plone.org/release/4.0a1/versions.cfgversions = versions
    find-links = http://dist.plone.org/thirdparty/PILwoTk-1.1.6.4.tar.gz
    parts = instance

    [instance]
    recipe = plone.recipe.zope2instance
    user = admin:admin
    eggs =
        PILwoTk
        Plone

Thanks framework team and core developers for this impressive release.

.. _Plone: http://plone.org
