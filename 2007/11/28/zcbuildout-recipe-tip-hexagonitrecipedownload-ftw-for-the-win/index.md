# hexagonit.recipe.download

Sometimes a Plone add-on is distributed as a compressed archive and is
extracted to the `foo/` directory but the Python package is named `bar`.
This can be a problem when using
[plone.recipe.distros](https://pypi.org/project/plone.recipe.distros/)
because when `bar` is extracted to `parts/productdistros/foo` the Plone
add-on will not be loaded by Zope.

Fortunately there is
[hexagonit.recipe.download](https://pypi.org/project/hexagonit.recipe.download/)
which allows you to specify the destination. For example,
[ZNagios](https://pypi.python.org/pypi/Products.ZNagios), an add-on that
integrates Zope with Nagios.

If we use
[plone.recipe.distros](https://pypi.org/project/plone.recipe.distros/)
we end up with ZNagios installed in `parts/productdistros/trunk`. But if
we use
[hexagonit.recipe.download](https://pypi.org/project/hexagonit.recipe.download/)
we end up with the contents of the compressed archive in
`products/ZNagios`.

E.g.

    [buildout]
    parts = znagios

    [znagios]
    recipe = hexagonit.recipe.download
    url = http://svn.gocept.com/viewcvs/ZNagios/trunk.tar.gz?view=tar
    destination = products/ZNagios
    strip-top-level-dir = True

After running Buildout you should have the following files in your
`products/` directory.

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

Awesome!
