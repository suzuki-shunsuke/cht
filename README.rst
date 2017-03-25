cht
===

Notify to the slack channel using the incoming webhooks when the
previous command has ended.

Requirements
------------

-  Python 2

Install
-------

pypi
~~~~

::

    $ pip install cht

Download
~~~~~~~~

If you don't want to install cht with pip, download the main script.

::

    # assume that ~/bin is included in $PATH
    $ curl https://raw.githubusercontent.com/suzuki-shunsuke/cht/master/main.py -o ~/bin/cht
    $ chmod a+x ~/cht

Usage
-----

::

    $ <previous command>; cht $? [-u <url>] [-c <channel>]

if you want to send the previous command's output to the slack channel,
use pipe.

::

    $ <previous command> | cht [-u <url>] [-c <channel>]

Environment Variable
--------------------

You can use the following environment variables to set the channel and
webhook url.

-  CHT\_URL: webhook url
-  CHT\_CHANNEL: channel name

Command line arguments are prefered to the environment variables.

Contributing
------------

1. Fork (https://github.com/suzuki-shunsuke/cht/fork)
2. Create a feature branch
3. Commit your changes
4. Rebase your local changes against the master branch
5. Create a new Pull Request

License
-------

`MIT <LICENSE>`__

Author
------

`Suzuki Shunsuke <https://github.com/suzuki-shunsuke>`__
