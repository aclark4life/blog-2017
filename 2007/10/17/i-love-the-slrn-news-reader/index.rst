I Love the ``slrn`` News Reader
===============================

.. post:: 2007/10/17

**A command line news reader.**

I've been meaning to write this blog entry about ``slrn`` ever since I started using it some time last year. Finally, here it is. Here are a few things I'd like you to know about ``slrn``:

- It rocks, for those that enjoy terminal applications as I do (e.g.  mutt, w3m, etc.)
- And by "rocks" I mean, it allows you to do in a terminal what most people do in a graphical application.
- Further, it allows you to do it the way you want (for the most part) and by that I mean, it allows you to bind keys to actions.
- It's a bit confusing to get started, that is what I'd like to help with here. There is a default config file that you'll want to copy to ~/.slrnrc.
- There are some additional configuration parameters I use that were hard to track down. Those are:

::
    set confirm_actions 14
    visible_headers "From:,Subject:,Newsgroups:,Followup-To:,Reply-To:,Date:"
    set query_read_group_cutoff 0
    set uncollapse_threads 1
    set netiquette_warnings 0

Most of these are self-explanatory, but if you are confused please see: http://slrn.sourceforge.net/manual/slrn-manual.html 
