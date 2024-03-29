# PythonPackages: One Year Later

::: {.post category="Pyramid, Python"}
2012/09/28
:::

**We are rolling up on the one year anniversary of pythonpackages.com
(in October).**

This is an exciting milestone (for me at least) because I\'ve had a
tremendous amount of fun building the site, not to mention how much I
learned about GitHub, PyPI, Pyramid, Stripe, Redis, Bootstrap, and more.

We are hovering around 200 signups which I\'m quite proud of. But in
terms of **possible-financial-success** i.e. the potential of converting
some of those sign ups in to actual customers I\'d feel better if we
were at 2,000 or higher.

## What happened?

As of the launch of the beta site 3 months ago, there are some
actually-useful features available:

-   The [ability to release a package from GitHub to
    PyPI](http://docs.pythonpackages.com/en/latest/introduction.html#introduction)
    without a terminal (i.e. in the web browser).
-   The ability to release a package with [git push]{.title-ref} (by
    adding the service:
    <https://github.com/github/github-services/blob/master/services/pythonpackages.rb>)
-   The ability to \"manage packages\" (see image below)

![alternate text](/images/manage-packages.png){.img-thumbnail
.img-thumbnailalign-center}

-   The ability to \"manage organizations\" (see image below)

![alternate text](/images/manage-organizations.png){.img-thumbnail
.img-thumbnailalign-center}

-   The [ability to create packages through the
    web](http://docs.pythonpackages.com/en/latest/create-package.html#create-packages)
    (i.e. from the web browser to GitHub, whereas normally you\'d run
    PasteScript in your Terminal).

![alternate text](/images/create-new-package.png){.img-thumbnail
.img-thumbnailalign-center}

And a few more logistical features that are cool:

-   The ability to pay with a credit card (via Stripe)

![alternate text](/images/pay-with-stripe.png){.img-thumbnail
.img-thumbnailalign-center}

-   The ability to oauth against PyPI:

![alternate text](/images/pypi-oauth.png){.img-thumbnail
.img-thumbnailalign-center}

Still, we have only scratched the surface of what could potentially be
provided to the Python community. Future plans include:

-   The ability to easily [build Windows
    installers](https://bitbucket.org/pythonpackages/pythonpackages.com/issue/28/build-windows-installers)
    for your Python software.
-   [Support for other
    services](https://bitbucket.org/pythonpackages/pythonpackages.com/issue/27/support-bitbucket-and-other-dvcs-services)
    e.g. bitbucket.
-   [Support git
    branches](https://bitbucket.org/pythonpackages/pythonpackages.com/issue/29/add-git-branch-support)
    i.e. for releasing from a branch.

In summary, this is a great start to building \"github style\"
automation for Python packaging but there is much more work to be done.

## What now?

I am in the process of winding down the 3 month \"beta 1\" period. The
\"beta 2\" period (from now until the end of the year) will likely
include:

-   Adding MailChimp integration to make it easier to email subscribers.
-   Turn off SSL to save \$20/month.
-   Write tests and open source the application.

## What can you do to help?

If you believe in the ideas behind pythonpackages.com (primarily:
eliminating the need to think about packaging at all; e.g. through task
automation, and process improvement behind the scenes; i.e. supporting
new technology like distutils2/packaging, wheel, et al.; in order to
present a seemless packaging story to developer-consumers.) then the
best thing you can do is to purchase a paid plan:

-   <http://pythonpackages.com/plans>

The second best thing you can do is support me on gittip:

-   <https://gittip.com/aclark4life>

These funds will go towards covering hosting costs until such time as
the service can pay for itself. I am also asking folks who appreciate my
open source work in general to consider a gittip donation. If you cannot
help financially, you can still use the free plan to release packages!
Please try it out and [give
feedback](https://bitbucket.org/pythonpackages/pythonpackages.com/issues/new).
(The paid plans get you access to more package slots, so you don\'t have
to swap out the free slot, and organizations, so you can release
packages from organization repos).

Thanks for considering!
