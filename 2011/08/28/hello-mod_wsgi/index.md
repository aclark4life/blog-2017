# Hello mod_wsgi

::: {.post category="Buildout, Plone"}
2011/08/28
:::

**It seems I\'ve inadvertently started another series of blog entry**

It seems I\'ve inadvertently started another series of blog entry: the
\"hello world\" series, wherein I explain how to easily get started with
[various exciting Python
technologies](http://blog.aclark.net/2011/08/20/hello-plone/).

This time, in order to familiarize myself with [mod\\\_wsgi](), I\'ve
created a buildout to automate some of the processes explained in:

-   <http://code.google.com/p/modwsgi/wiki/QuickInstallationGuide>

(This series also helps me to subtly introduce the zc.buildout
\"extendables\" I have been working on. More on those in a future post.)

## The extendables

The extendables make it easy to bootstrap a development environment with
complex software requirements, via
[zc.buildout](http://pypi.python.org/pypi/zc.buildout/1.5.2). In this
case, I want to be able to type:

    $ test-apache test-dir

And get a working, *disposable* Apache instance minutes later. I also
want that Apache to come with a mod_wsgi app installed and working.

## Setup

First we use the [aforementioned
extendable](https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/2.2.x),
like so:

    $ virtualenv test-dir
    $ cd test-dir
    $ bin/pip install zc.buildout
    $ bin/buildout init

Edit the buildout.cfg to look like this:

    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/2.2.x 

Run buildout:

    $ bin/buildout

Assuming successful completion, you should be able to run Apache in the
foreground via:

    $ bin/supervisord -e debug -n

Now check <http://localhost:8080>.

This works because the [\"extendable\" (buildout configuration
file)](https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/2.2.x)
contains:

-   The [little WSGI
    app](https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/conf/app.wsgi.in)
    from the QuickInstallationGuide, templatized via
    [collective.recipe.template](http://pypi.python.org/pypi/collective.recipe.template/1.9).
-   A [templatized httpd.conf
    file](https://github.com/ACLARKNET/build/blob/master/apache/2.2.x/httpd.conf.in).

I like to automate the process even further with the [following
script](https://github.com/ACLARKNET/binfiles/blob/master/test-apache):

    #!/bin/shmkdir $1
    virtualenv-2.6 $1
    cd $1
    bin/easy_install zc.buildout
    bin/buildout init
    cat << EOF > buildout.cfg
    [buildout]
    extends = https://raw.github.com/pythonpackages/buildout-apache-modwsgi/master/2.2.x
    EOF
    bin/buildout
    bin/supervisord -e debug -n

Thus closing the loop on this blog entry, and making the following
possible:

    $ test-apache test-dir

I\'ve been using my
[test-plone](https://github.com/ACLARKNET/binfiles/blob/master/test-plone)
script for years now, and I\'m hoping that the test-apache script proves
just as useful (especially as Plone moves closer to a WSGI-supporting
stack via [Zope 2.13](http://pypi.python.org/pypi/Zope2/2.13.9)).
