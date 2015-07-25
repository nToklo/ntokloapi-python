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

Products
--------

To keep track of the products, you have to send them first. **It's not a
requirement** but if you have a big catalog it will allow you to preprocess
the data before starting to send events.

Example:

.. code-block:: python
   :linenos:

    import ntokloapi

    uv = {
        "version": "1.2", # If this doesn't exist, the connector will assume latest
        "product": {
            "id": "10201",
            "category": "Shoes",
            "manufacturer": "Nike",
            "currency": "GBP",
            "unit_sale_price": 98
        },
    }

    product = ntokloapi.Product(MyAPIKey, MyAPISecret)

    # If you want to send the product straight to the API
    product.create(uv)

    # In case you want to check the response
    response = product.create(uv)
    print(response)  # HTTP 204 is the expected output

Events
------

An event in the nToklo recommendation system means some kind of action that has
performed by the user, and it.

Example:

.. code-block:: python
   :linenos:

    import ntokloapi

    # This UV is a bit special. You can send the minimum data as in the
    # example, but you can expend it with the whole information about the
    # product and the user if you want. That way if the product doesn't exist
    # it will be automatically created in the API.

    uv = {
        "version": "1.2", # If this doesn't exist, the connector will assume latest
        "user": {
            "user_id": "112"
        },
        "product": {
            "id": "10201",
        },
        "events": [
            {
                "action": "preview",
                "category": "conversion_funnel"
            }
        ]
    }

    event = ntokloapi.Event(MyAPIKey, MyAPISecret)

    # In case you want to send it straight to the API
    event.send(uv)

    # In case you want to check the response
    response = event.send(uv)
    print(response)  # HTTP 204 is the expected output

Recommendations
---------------

This is the core of the system, the recommendations. This function will return
to you a JSON object withe the recommended products for your user and a temporary token.

Example:

.. code-block:: python
   :linenos:

    import ntokloapi

    recommendation = ntokloapi.Recommendation(MyAPIKey, MyAPISecret)
    recommendations = recommendations.get(productid='10201')

    print(recommendations)

It should return something like this:

.. code-block:: python
   :linenos:

    {
        "tracker_id": "1d9042f0-32d3-11e5-88b8-19d6b5557055",
        "items": [
            {
                "id": "10201",
                "category": "Shoes",
                "manufacturer": "Nike"
            }
        ]
    }


Blacklist
---------

The blacklist functionality allows you to add products to a blacklist so they
don't show up on the recommendations.

Example:

.. code-block:: python
   :linenos:

    import ntokloapi

    blacklist = ntokloapi.Blacklist(MyAPIKey, MyAPISecret)

    # Add one product to the blacklist
    blacklist.add(['10201',])

    # Add multiple rpoducts to the blacklist
    blacklist.add(['10201', '10202', '10203'])

    # Remove a product from the blacklist
    blacklist.remove(['10203',])

    # Remove multiple products from the blacklist
    blacklist.add(['10201', '10202'])

    # List all the currently blacklisted products
    blacklisted_products = blacklist.list()
    print(blacklisted_products)

Charts
------

Charts allows you to pull information regarding your analytics. It's not a
full report, for that you will have to use the `nToklo Console <http://console.ntoklo.com>`_. Charts contains a number of options that will be useful to you
for filtering the information. Please refer to the :doc:`reference`.

.. code-block:: python
   :linenos:

    import ntokloapi

    charts = ntokloapi.Chart(MyAPIKey, MyAPISecret)
    analytics = charts.get(date='1364169600000')

    print(analytics)
