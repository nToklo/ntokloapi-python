Installation
============

To install the nToklo API connector you can do it trough pip:
::

    $ pip install ntokloapi

If you want to install the latest version from the git repository you can
do it like this:
::

    $ pip install git+https://github.com/nToklo/ntokloapi-python

Once you have installed it, you can import it like any other module:
::

    import ntokloapi

You can access the functionality like this:
::

    event = ntokloapi.Event(key, secret)
    event.send(uv)


