UNIX Tips For The Elderly
=========================

.. post:: 2008/03/06

I often want to do ***something*** to a bunch of files on the filesystem, e.g.

.. raw:: html

    <style>
    pre:before .prompt { content: '$ ' }
    </style>

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

::

    $ find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % ls -d %
    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a

or

::

    $ find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % file %
    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a:
      ISO Media, MPEG v4 system, iTunes AAC-LC

... and afterwards go back to whatever I was supposed to be working on in the first place. There, I feel better now! Thanks for listening,

 

:-)

 

P.S. If anyone knows a better way to do this, please add it in the comments.
