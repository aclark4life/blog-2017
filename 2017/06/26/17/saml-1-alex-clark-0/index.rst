SAML: 1, Alex Clark: 0
======================

.. post:: 2017/06/26
    :category: Django, Python

|

**Update: OOPS looks like this one got away from me (got published prematurely). I meant to write about Django & SAML about a month ago. Here is that post finally.**

|

.. image:: /images/saml-failure-complete.jpg
    :alt: Courtesy of quickmeme

*Courtesy of* `quickmeme <http://www.quickmeme.com/>`_

|

Intro
-----

**I don't like to give up on a technical challenge**, particularly when the progress is slow-but-consistent. It's only when I know I can't make any discernible progress easily (or at all) that I can force myself to give up. I'm not talking about giving up for the day and getting back to it. I'm talking about declaring failure and getting back to it WAY later, if at all. Well, this post is about how SAML got the better of me about one month ago. I really wanted this particular task to be successful, but I eventually had to give up and declare the task "too hard for me given the context, and possibly not even a good idea in the first place".

Because I don't explicitly mention this anywhere else in the article, I'll mention it now: SAML is used to implement "single sign on". (Cue debate on merits of this approach vs. other approaches e.g. OAuth2.)

The task
--------

**The task was to make Django act as a SAML Identity Provider (IdP)**, enough to convince a commercial service, acting as a SAML Service Provider (SP), to use it as one. While I didn't achieve the desired end result, a learned a ton of information about SAML that I never really wanted to know, but feel better and good about now that I know it.

IdP vs SP
---------

I'm not going to go into too much detail here but for the unfamiliar, the SAML protocol defines both Identity Providers (IdP) and Service Providers (SP). SAML Identity Providers answer requests from SAML Service Providers and make the decision about whether the principal (e.g. user) is allowed to access the Service Provider.

After discovering this fact, confusion about this aspect of the SAML protocol lingered and continues to linger. Does that mean the IdP *is* or *contains* the user database? As of right now, I don't think so. But that wasn't clear initially (and still isn't, but perhaps is now "less unclear").

**No, the IdP is not the user database.** Rather, the IdP is "the thing that answers SAML requests in accordance with the protocol's definition of how to do so." But it can't hurt if the IdP needs to go no further than Django's user database to validate an SP's SAML assertion, right? I certainly thought so initially, and spent a whole lot of time trying to make it so.

XML
---

Turns out implementing SAML presents many challenges, one of which is one must "deal with" XML. I don't have any specific gripes about XML, but parsing XML does add a **layer of complexity I could have done without**.

Crypto
------

You know what's worse than parsing XML? Signing your XML. And you know what's worse than that? **Signing only a portion** of it. (Lingering bitter sentiments from the me-of-one-month-ago.)

Django
------

First, I spent some time researching the existing available options. I took it as a "red flag" not a lot of folks seemed to be using Django as an IdP, but I thought worst case, I'd be creating an insecure-but-viable-proof-of-concept. And I got close, but lost patience when I couldn't get the commercial Service Provider to validate my SAML assertions (oh, and let's not forget my confusion about SP-initiated vs IdP-initiated logins; I eventually decided that the "flow" of IdP-initiated was simpler and focused mostly on that; SP -> IdP -> SP, vs IdP -> SP.)

Eventually **I created five, count them five, separate repositories while tackling SAML**. Part of that proliferation-of-repositories is *possibly* due to some anti-branching sentiment on my part (I'm not anti-branching, but sometimes I prefer to "start clean" instead of branching):

- https://github.com/aclarktest/django-saml2-sp (Fork of an existing repository that works great as a proof of concept along with https://github.com/aclarktest/django-saml2-idp)
- https://github.com/aclarktest/django-saml2-idp (Fork of an existing repository that works great as a proof of concept along with https://github.com/aclarktest/django-saml2-sp)
- https://github.com/aclarktest/django-saml2-test (Where most of my research occurred.)
- https://github.com/aclarktest/django-samlicious (Let's start over with lessons learned in a new app.)
- https://github.com/aclarktest/dj-sam (Let's start over again, with a slightly different approach. And here the effort dies; relics remain as a cautionary tale to passersby.)

Python
------

I found a bunch of cool Python tooling for dealing with all-things-SAML that I will make a note of here:

- https://github.com/onelogin/python-saml (python-saml on PyPI, not to be confused with https://github.com/mehcode/python-saml)
- https://github.com/mehcode/python-saml (saml on PyPI)
- https://github.com/dlitz/pycrypto (secure hash functions!)

TL;DR: Consider a commercial IdP like OneLogin or Auth0.
