Buildout Recipe Tip: ``hexagonit.recipe.download``
==================================================

.. post:: 2007/11/28
    :category: Buildout, Plone, Python

**How to handle difficult old-style add-ons.**

Sometimes an "old-style" add-on is distributed as ``foo.tar.gz`` and extracts to ``foo/``, but the package is called ``bar``. This can be a problem when using the ``plone.recipe.productdistros`` recipe because when ``bar`` is extracted to ``parts/productdistros/foo`` it will not work.

Fortunately there is ``hexagonit.recipe.download``, which allows you to specify the destination. For example, `ZNagios <https://pypi.python.org/pypi/Products.ZNagios>`_ (an add-on that integrates Zope with Nagios) is available as a tarball here:

- http://svn.gocept.com/viewcvs/ZNagios/trunk.tar.gz?view=tar

If we use productdistros, we end up with ZNagios installed in ``parts/productdistros/trunk``. But if we use ``hexagonit.recipe.download`` we can control the destination.

::

    [buildout]
    parts = znagios

    [znagios]
    recipe = hexagonit.recipe.download
    url = http://svn.gocept.com/viewcvs/ZNagios/trunk.tar.gz?view=tar
    destination = products/ZNagios
    strip-top-level-dir = True

After running Buildout you should have the following in your ``products/`` directory:

::

    /products/ZNagios
    /products/ZNagios/COPYRIGHT.txt
    /products/ZNagios/LICENSE.txt
    /products/ZNagios/README.txt
    /products/ZNagios/__init__.py
    /products/ZNagios/check_zope.py
    /products/ZNagios/munin_client.py
    /products/ZNagios/version.txt
    /products/ZNagios/zeo_munin.py
    /products/ZNagios/zope.cfg
