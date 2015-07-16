Usage
=====

To use the ntokloapi connector you just need to import it:
::

    import ntokloapi

Then you will have access to the different parts of the API. Remember that to
interact with the API you will need a valid API key and API secret.

Universal Variable
------------------

The nToklo recommendation engine uses UV (Universal Variable) objects to create
the recommendations. UV is a type of JSON object that has a specific set of
keys to manage ecommerce entries. You can check the specification `here <http://docs.qubitproducts.com/uv/>`_.


Events
------

An event in the nToklo recommendation system means some kind of action that has
performed by the user, and it

Example data:
::

    {
        "version": "1.2", # If this doesn't exist, the connector will assume latest
        "user": {
            "user_id": "112"
        },
        "product": {
            "id": "10201",
            "category": "Shoes",
            "manufacturer": "Nike"
        },
        "events": [
            {
                "action": "preview",
                "category": "conversion_funnel"
            }
        ]
    }

::

    import ntokloapi

    event = ntokloapi.Event(apikey, apisecret)
    event.send(uv)
