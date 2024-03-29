# Updated Django Website

::: {.post category="Django, Python"}
2016/02/21
:::

**One year later**

![image](/images/aclarknet-website.png){.img-thumbnail
.img-thumbnailalign-center}

| 

Last year I wrote about developing our company website with Django:

-   <http://blog.aclark.net/2015/01/11/new-django-website/index.html>

This year, I updated the site and am again very happy with the results.
Here\'s an overview of the interesting aspects.

## Makefile

I\'ve continued to develop Python projects using a `Makefile`. So much
so I\'m now attempting to genericize the approach here:

-   <https://github.com/aclark4life/python-project>

## Project/App

Last year around this time I didn\'t fully understand what I was doing
with `startproject` and `startapp` (as evidenced by [this insanely
nested package
structure](https://github.com/ACLARKNET/aclarknet-django/tree/master/aclarknet/aclarknet/aclarknet)).
Now I understand a little bit more, so I settled on a project called
`aclarknet` and an app called `website`.

## REST-powered

I haven\'t written about it yet, but I spent a lot of time in December
developing a [time tracking and invoicing
application](https://github.com/ACLARKNET/aclarknet-database) (more on
that later). As such, I couldn\'t tolerate storing identical data in
multiple locations. So [exposed the data I
needed](https://github.com/ACLARKNET/aclarknet-database/blob/master/aclarknet/database/serializers.py)
via Django Rest Framework [then consumed it with
requests](https://github.com/ACLARKNET/aclarknet-website/blob/master/aclarknet/website/views.py#L37).

## Other nice features

-   Django 1.9.2
-   Bootstrap 3.3.6
-   Logo created with Illustrator (IANAGA, but it was [fun to
    try](https://github.com/ACLARKNET/aclarknet-logo)).

Enjoy the [site](http://aclark.net) and
[code](https://github.com/ACLARKNET/aclarknet-website) and [hire my
business](http://aclark.net/contact) in 2016!
