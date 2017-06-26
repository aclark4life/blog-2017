SAML: 1, Alex Clark: 0
======================

.. post:: 2017/06/26
    :category: Python

*Update: OOPS looks like this one got away from me. I meant to write about SAML about a month ago. Here is that post.*

|

Intro
-----

I don't like to give up on a technical challenge, particularly when the progress is slow-but-consistent. It's only when I know I can't make any discernible progress easily (or at all) that I can force myself to give up. I'm not talking about giving up for the day and getting back to it. I'm talking about declaring failure and getting back to it WAY, later if at all. Well, this post is about how SAML got the better of me about one month ago. I really wanted this particular task to be successful, but I eventually had to give up and declare the task "too hard for me given the context and possibly not even a good idea in the first place".

The task
--------

The task was to make Django act as an IdP, enough to convince a commercial service to use it as one. While I didn't achieve the desired end result, a learned a ton of information about SAML that I never really wanted to know, but feel better and good about now that I know it.

IdP vs SP
---------

I'm not going to go into too much detail but for the unfamiliar, the SAML protocol defines both "identity providers" and "service providers". SAML identity providers answer requests from SAML service providers and make the decision about whether the principal (e.g. user) is allowed to access the service provider.



XML
---

Crypto
------

Django
------



TL;DR: Choose a commercial IdP like OneLogin.
