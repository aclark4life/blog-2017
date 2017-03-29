UNIX Tips For The Elderly
=========================

.. post:: 2008/03/06
    :category: Misc

.. image:: /images/huh.png

.. raw:: html

    <style>
    pre.prompt:before { content: '$ ' }
    </style>


**I often want to do something to a bunch of files on the filesystem.**

E.g.

.. raw:: html

    <pre class="prompt">
    find Music/ | xargs -J % echo 'Do something to ' %
    </pre>

The problem is that sometimes the filenames have spaces in them which will cause:

.. raw:: html

    <pre class="prompt">
    find Music/ | xargs -J % 'Do something to ' %
    </pre>

::

    xargs: unterminated quote

Useless. The best fix I've managed to come up with which I couldn't recall hence the blog post, is to replace the beginning and end of the line with quotes to make the shell happy, e.g.

.. raw:: html

    <pre class="prompt">
    find Music/ | sed -e 's/^/"/' -e 's/$/"/'
    </pre>

::

    "Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a"

So I can do things like:

.. raw:: html

    <pre class="prompt">
    find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % ls -d %
    </pre>

::

    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a

or

.. raw:: html

    <pre class="prompt">
    find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % file %
    </pre>

::

    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a: ISO Media, MPEG v4 system, iTunes AAC-LC
