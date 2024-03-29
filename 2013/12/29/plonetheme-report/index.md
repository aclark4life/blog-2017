# Plonetheme Report

::: {.post category="Buildout, Plone"}
2013/12/29
:::

**Here is another report on Plone themes.**

Here is another report on Plone themes[^1] generated by plock[^2]

::

:   #!/bin/sh for i in [plock -l -r \| grep plonetheme]{.title-ref} do
    plock . -a \$i done

Plock is able to produce a Buildout configuration file containing all
themes that successfully installed via Buildout; I manually removed the
themes that caused Plone start to fail.

## Before Plone start

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3

    [plone]
    eggs = 
        ${addon:packages}
        ${base:packages}
        plonetheme.ReOrg
        plonetheme.aclark_twitter
        plonetheme.aqueouslight
        plonetheme.arnolfini
        plonetheme.bananaleaf
        plonetheme.basic
        plonetheme.bluegray
        plonetheme.burned
        plonetheme.classic
        plonetheme.cleantheme
        plonetheme.codapress
        plonetheme.colorfulworld
        plonetheme.coolblue
        plonetheme.criticas
        plonetheme.cultureCab
        plonetheme.darkened
        plonetheme.delicious2
        plonetheme.diazo_sunburst
        plonetheme.discovery
        plonetheme.drupal
        plonetheme.earthlingtwo
        plonetheme.evergreen
        plonetheme.ewb_case
        plonetheme.freshpick
        plonetheme.fui
        plonetheme.gemstone
        plonetheme.gov
        plonetheme.greencommunity
        plonetheme.grungeera
        plonetheme.html5_hotpink
        plonetheme.inbusiness
        plonetheme.intk
        plonetheme.jsjamba
        plonetheme.keepitsimple
        plonetheme.laboral
        plonetheme.labs
        plonetheme.leavesdew
        plonetheme.level2
        plonetheme.mimbo
        plonetheme.mvob
        plonetheme.netsightintranet
        plonetheme.nonzero
        plonetheme.notredame
        plonetheme.overlappedtabs
        plonetheme.p2
        plonetheme.ploneorg
        plonetheme.porseleinplaats
        plonetheme.pyar
        plonetheme.rcom
        plonetheme.redmusic
        plonetheme.relic
        plonetheme.responsive1140
        plonetheme.responsivetheme
        plonetheme.solemnity
        plonetheme.stylized
        plonetheme.subordinate
        plonetheme.sunburst
        plonetheme.terrafirma
        plonetheme.tidyblog
        plonetheme.transition
        plonetheme.twinapex
        plonetheme.unilluminated
        plonetheme.wmoWonen
        plonetheme.woodexperience
        plonetheme.xtheme
        sphinx.plonetheme
        vs.bootstrap.plonetheme

## After Plone start

    [buildout]
    extends = https://raw.github.com/plock/pins/master/plone-4-3

    [plone]
    eggs = 
        ${addon:packages}
        ${base:packages}
        plonetheme.ReOrg
        plonetheme.aclark_twitter
        plonetheme.aqueouslight
        plonetheme.bananaleaf
        plonetheme.basic
        plonetheme.bluegray
        plonetheme.burned
        plonetheme.classic
        plonetheme.cleantheme
        plonetheme.codapress
        plonetheme.colorfulworld
        plonetheme.coolblue
        plonetheme.criticas
        plonetheme.cultureCab
        plonetheme.darkened
        plonetheme.delicious2
        plonetheme.diazo_sunburst
        plonetheme.discovery
        plonetheme.drupal
        plonetheme.earthlingtwo
        plonetheme.evergreen
        plonetheme.ewb_case
        plonetheme.freshpick
        plonetheme.fui
        plonetheme.gemstone
        plonetheme.greencommunity
        plonetheme.grungeera
        plonetheme.html5_hotpink
        plonetheme.inbusiness
        plonetheme.jsjamba
        plonetheme.keepitsimple
        plonetheme.labs
        plonetheme.leavesdew
        plonetheme.level2
        plonetheme.mimbo
        plonetheme.nonzero
        plonetheme.notredame
        plonetheme.overlappedtabs
        plonetheme.p2
        plonetheme.ploneorg
        plonetheme.pyar
        plonetheme.rcom
        plonetheme.redmusic
        plonetheme.relic
        plonetheme.responsive1140
        plonetheme.responsivetheme
        plonetheme.solemnity
        plonetheme.stylized
        plonetheme.subordinate
        plonetheme.sunburst
        plonetheme.terrafirma
        plonetheme.tidyblog
        plonetheme.transition
        plonetheme.twinapex
        plonetheme.unilluminated
        plonetheme.woodexperience
        plonetheme.xtheme
        sphinx.plonetheme
        vs.bootstrap.plonetheme

## Removed themes

    plonetheme.arnolfini
    plonetheme.gov
    plonetheme.intk
    plonetheme.laboral
    plonetheme.mvob
    plonetheme.netsightintranet
    plonetheme.porseleinplaats
    plonetheme.wmoWonen

Not bad! That\'s a lot of working themes for Plone 4, many of which use
Diazo.

![alternate text](/images/plonetheme-report-1.png){.img-thumbnail
.img-thumbnailalign-center}

![alternate text](/images/plonetheme-report-2.png){.img-thumbnail
.img-thumbnailalign-center}

![alternate text](/images/plonetheme-report-3.png){.img-thumbnail
.img-thumbnailalign-center}

[^1]: In the `plonetheme` namespace.

[^2]: Plock is a Plone installer for the pip-loving crowd:
    <https://plock.github.com>.
