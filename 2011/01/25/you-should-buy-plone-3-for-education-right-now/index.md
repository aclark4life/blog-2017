# You Should Buy Plone 3 for Education Right Now

::: {.post category="Plone"}
2011/01/25
:::

**With what must be the fifth or sixth round of apologies to both Erik
Rose and PACKT publishing for the delay (very sorry guys), here is my
review! Better late than never.**

I get bored with the same ol\' blog entry titles:

> \"A review of so and so\'s book, by such and such...\"

Not that there is anything wrong with these titles, they serve their
purpose. It\'s not you... it\'s me. Can we still be friends?

Anyway, I will cut to the chase with this one: if you care about Plone
and you have not done so already, you should buy **\`Plone 3 for
Education\`\_**right now.

Why?

Several reasons:

-   Erik Rose cares about Plone. He cares so much, he spent months of
    his life pouring his professional experiences into a book so you can
    benefit!
-   PACKT publishing will donate a percentage of the proceeds to the
    [Plone Foundation.](http://plone.org/foundation)
-   You will learn a lot about Plone, from the perspective of someone
    who has supported its deployment and maintenance within a large
    educational institution.

That is not to say every Plone book is for you. You have to decide for
yourself if you want this beautiful creation (see above) of Erik\'s to
shine on your mantle piece for years to come. Even if you are a giant
Plone supporter, and even if you make your living off of Plone, you may
still not want to purchase this book. That\'s just the way that it goes.
But, I will to try to convince you anyway! Here is my chapter-by-chapter
review:

## Preface

The preface sets the tone of the book, and I like the tone Erik sets.
Erik has used Plone for many years at [Penn
State](http://weblion.psu.edu/) and you will find his experiences
valuable. He\'s made mistakes so you don\'t have to!

## Chapter 1

Chapter 1 covers creating courses (of course!) Erik makes the argument
that Plone can hold it\'s own against expensive course management
software, and I believe him. Of particular interest are Erik\'s
recommendations to:

-   Put courses in large Plone folders
-   Use news items, events and collections in the context of a course.
-   Cut and paste the course framework once you are done creating it.

## Chapter 2

Chapter 2 introduces calendaring in Plone, and Erik suggests using
[Plone4artists calendar](http://pypi.python.org/pypi/p4a.plonecalendar)
to make your course content easily browsable. Of particular interest are
Erik\'s recommendations to:

-   Replace the stock Plone events folder (which is a collection
    contained within a folder) with (just) a collection.
-   Make clever use of keywords to support lots of events.
-   Reorder subfolders in a collection \"the hard way\". (Also
    interesting that he opened this ticket:
    <https://dev.plone.org/plone/ticket/9109>and that it has received no
    \"love\" to date. Perhaps the new collections UI:
    <http://dev.plone.org/plone/ticket/10902> will save the day!)

## Chapter 3

Chapter 3 showcases the [Faculty/Staff
Directory](http://pypi.python.org/pypi/Products.FacultyStaffDirectory)
(FSD) add-on for Plone which allows you to create an online personnel
directory. Of particular interest is Erik\'s explanation of how to
categorize and correlate people within FSD.

## Chapter 4

Chapter 4 covers customizing Faculty/Staff Directory. Of particular
interest is Erik\'s coverage of [AT Schema
Extender](http://pypi.python.org/pypi/archetypes.schemaextender)(which
is a great way to customize Plone these days).

## Chapter 5

Chapter 5 covers blogs and forums. Of particular interest is Erik\'s
coverage of [Scrawl](http://pypi.python.org/pypi/Products.Scrawl), and
the need to exercise extreme caution when installing add-ons (always
good advice).

## Chapter 6

Chapter 6 covers audio and video. Of particular interest is Erik\'s
coverage of
[collective.flowplayer](http://pypi.python.org/pypi/collective.flowplayer)
which makes [Flowplayer](http://flowplayer.org/) easy to use in Plone.

## Chapter 7

Chapter 7 covers forms. Of particular interest is Erik\'s comparison of
[PloneFormGen](http://pypi.python.org/pypi/Products.PloneFormGen) to
Archetypes content objects, and his explanation of when to use one over
the other.

## Chapter 8

Chapter 8 covers theming. Of particular interest is Erik\'s coverage of
\"new style\" template customizations via
[z3c.jbot](http://pypi.python.org/pypi/z3c.jbot) (which you [don\'t even
need a package
for!](https://github.com/aclark4life/aclark_net_website/blob/master/buildout.cfg#L24))

## Chapter 9

Chapter 9 covers deployment. Of particular interest is Erik\'s coverage
of a typical production software stack that includes ZEO, Zope2, Apache
and of course Plone. Also covered is CacheFu, which has been superseded
by [plone.app.caching](http://pypi.python.org/pypi/plone.app.caching) in
Plone 4.

## Chapter 10

Chapter 10 covers maintenance. Of particular interest is Erik\'s
coverage of
[collective.recipe.backup](http://pypi.python.org/pypi/collective.recipe.backup)
to automate the creation of repozo scripts. I would add to that, you can
use
[z3c.recipe.usercrontab](http://pypi.python.org/pypi/z3c.recipe.usercrontab)to
automate the creation and removal of cron jobs to execute those scripts.

## Conclusion

All in all, I enjoyed reading this book. And, I appreciate whenever a
member of the community shares his/her experiences. So thank you, Erik!

That\'s it! I hope you will consider purchasing a copy of [Plone 3 for
Education](https://www.packtpub.com/plone-3-for-education/book) right
now.

*And if you enjoyed reading this review, please consider \`helping me
help Plone in February 2011.\`\_*

Alex Clark (January 2011)
