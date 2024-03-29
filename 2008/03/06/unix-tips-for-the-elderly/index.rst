UNIX Tips For The Elderly
=========================

Do something to a bunch of files
--------------------------------

I often want to do something to a bunch of files on the local filesystem. For example

::

    $ find Music/ | xargs -I % echo 'Do something to ' %

The problem is that sometimes the filenames have spaces in them which will cause

::

    $ find Music/ | xargs -I % 'Do something to ' %
    xargs: unterminated quote

Useless. The best fix I've managed to come up with which I couldn't recall hence the blog post, is to replace the beginning and end of the line with quotes to make the shell happy.

::

    $ find Music/ | sed -e 's/^/"/' -e 's/$/"/'
    "Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a"

So I can do things like this.

::

    $ find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % ls -d %
    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a

Or this.

::

    $ find Music/ | sed 's/^/"/' | sed 's/$/"/' | xargs -J % file %
    Music//iTunes/iTunes Music/Yael Naïm/Yael Naïm/03 New Soul.m4a: ISO Media, MPEG v4 system, iTunes AAC-LC

Awesome!
