A Shout Out to Shout IRC
========================

.. post:: 2016/12/15
    :category: Plone, Python

**I'm back on IRC for the foreseeable future, and loving it. Thank you Shout IRC.**

|

.. image:: /images/shout-irc2.png
    :align: center
    :class: img-thumbnail

|

Backlog
-------

A few years ago, I got old and gave up running command line IRC clients. I've run them all or at least a lot of them, including one `whose name is almost certainly in the crosshairs of political correctness <http://www.bitchx.com/>`_. Most recently I ran Weechat and irssi before that. For a while, I gave up IRC completely because I couldn't be bothered. But I missed it, and nothing else seemed to suffice. I tried Slack and thought it was OK, but not IRC. I tried various web clients, but couldn't find one I could stand to use long term. Then `Shout IRC <http://shout-irc.com/>`_ came along.

Stay online
-----------

I tried Shout for the first time over a year ago, but never bothered to create a Shout account on my server. This was a mistake, since user account creation enables one of Shout's most powerful features: `Stay online on IRC even when you log out <http://shout-irc.com/docs/server/users.html>`_.

Configuration
-------------

I had gotten annoyed with having to login each time, so I stopped using Shout for a while. I heard good things about Kiwi, but was disappointed to see `no npm release <https://www.npmjs.com/package/kiwiirc>`_. This led me back to Shout, which `does have an npm release <https://www.npmjs.com/package/shout>`_. What follows are configuration details for `irc.aclark.net <https://irc.aclark.net>`_, for posterity. (I added `Let's Encrypt <https://letsencrypt.org>`_ at the last minute for good measure.)

|

.. image:: /images/shout-irc1.png
    :align: center
    :class: img-thumbnail

|

AWS
~~~

- EC2 t2.micro running Ubuntu 16.04.1 LTS

Ubuntu
~~~~~~

::

    apt-get install aptitude
    aptitude update; aptitude upgrade -y
    aptitude install nginx nodejs-legacy npm python python-pip

Python
~~~~~~

::

    sudo -H pip install dotfiles

JavaScript
~~~~~~~~~~

::

    sudo npm install -g shout

Certbot (Let's Encrypt)
~~~~~~~~~~~~~~~~~~~~~~~

::

    sudo certbot certonly --manual

NGINX
~~~~~

::

    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;
        return 301 https://$host$request_uri;
    }
    server {
        listen 443 ssl default_server;
        listen [::]:443 ssl default_server;
        root /var/www/html;
        server_name _;
        location / {
            proxy_pass http://localhost:9000;
        }
        location /.well-known/acme-challenge/AamTqX-Ic-YERnU0RWS2X_WpszSUsi2lIoXkMYOy_Fs {
            add_header Content-Type text/plain;
            return 200 "AamTqX-Ic-YERnU0RWS2X_WpszSUsi2lIoXkMYOy_Fs.gPCswvmAzfObWoqUg6d_…";
        } 
        ssl    on;
        ssl_certificate    /etc/ssl/fullchain.pem;
        ssl_certificate_key    /etc/ssl/privkey.pem;
    }

Dotfiles
~~~~~~~~

(I store my ``.shout`` directory, which includes my Shout & Freenode credentials, in a private dotfiles repository.)

::

    git clone git@bitbucket.org:aclark4life/dotfiles.git Dotfiles
    dotfiles -s


Todo
----

I'm currently running ``shout --private`` in `screen <https://www.gnu.org/software/screen/>`_, but may eventually add a `systemd <https://www.freedesktop.org/wiki/Software/systemd/>`_ service for it.

|
