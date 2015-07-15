# nToklo API Python connector

Version: 0.1 alpha

This library will allow you to connect to the nToklo API and create your own applications, get tokens and the results.

## Installing

To install this library, you can do it through pip:

    $ pip install ntokloapi-python

If you want the latest version from the repository you can do:

    $ pip install git+https://github.com/nToklo/ntokloapi-python

## Usage

To use the nToklo API connector:
::

    from ntokloapi.events import Event

    payload = {"user": {"user_id": "112"},"product": {"id": "10201","category": "Shoes","manufacturer": "Nike"},"events": [{"action": "preview","category": "conversion_funnel"}]}

    event = Event(<myAPIKey>, <myAPISecret>)

    event.send(payload)

## License

This library is licensed under the Apache 2.0 license. See LICENSE for more
details

## Copyright

Copyright 2015 nToklo Ltd.
