# Zope2 Bootstrap

::: {.post category="Plone"}
2012/06/12
:::

**Bootstrap all the things, including Zope2.**

[zope2\\\_bootstrap]() is a new Python package that [monkey
patches](http://pypi.python.org/pypi/collective.monkeypatcher) Zope2 in
order to:

-   Replace [manage\\\_page\\\_styles.css.dtml]() styles with [Twitter
    Bootstrap](http://twitter.github.com/bootstrap/base-css.html)
    styles.
-   Adds CSS classes to
    [main](http://zope3.pov.lt/trac/browser/Zope/trunk/src/OFS/dtml/main.dtml)
    and/or [manage\\\_main]() tables.
-   Inserts a Plone logo (if Plone is installed) above
    [manage\\\_tabs.dtml]() tabs (h/t:
    <https://github.com/plone/Products.CMFPlone/blob/master/Products/CMFPlone/patches/addzmiplonesite.py>).
-   Inserts a ZMI warning (if Plone is installed) below
    [manage\\\_tabs.dtml]() tabs.

In the next version, I\'ll try to import [Twitter Bootstrap
JavaScript](http://twitter.github.com/bootstrap/javascript.html) for
even more goodness. Enjoy, and give feedback in the comments, or
[here](https://github.com/aclark4life/zope2_bootstrap/issues).
