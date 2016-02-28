Spaces Fixed
============

.. post:: 2008/03/06
    :category: Misc

**Thanks Apple.**

For those of you using Spaces in Mac OS X I'd like to follow up my previous post with some exciting news regarding Spaces in Mac OS X 10.5.2: it's fixed! Thousands of former FVWM users can now rejoice as they enjoy sane desktop pager functionality again. As you know, I've been using "Spaces... Spaces... Spaces..." and I just noticed that the issue has actually been resolved by Apple. See this post on macosxhints.com for more information: http://www.macosxhints.com/article.php?story=2008021122525348. To alter the annoying spaces-follows-application behavior do this:

.. raw:: html

    <style>
    pre:before { content: '$ ' }
    </style>

    <pre> 
    defaults write com.apple.dock workspaces-auto-swoosh -bool NO
    </pre>
    <pre> 
    sudo killall Dock
    </pre>
