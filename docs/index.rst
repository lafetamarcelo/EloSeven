.. Elo7Interview documentation master file, created by
   sphinx-quickstart on Sun Feb 28 16:26:23 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Elo7 Interview Project |:hand_with_index_and_middle_finger_crossed:|
====================================================================

Identification |:raised_hand_with_part_between_middle_and_ring_fingers:|
-------------------------------------------------------------------------

Hello, this is just an identification to link you with my curriculum |:smiley:|. My name is 
**Marcelo Mendes Lafetá Lima**. If there are any doubts considering what was done, please 
contact me at *marcelolafeta.nsee@gmail.com*. Thank very much for the oportunity!! Without 
further delongs lets start...

Summary
-------

The main goal of this documentation is to provide you with the information necessary to
at least understand the code developed and to use the API to predict the categorie of a
particular product, based open some pre defined information of this product. First of all
I will introduce how to access the API wich should be online in my Google Cloud App Engine.
And finally I will breaf you to the main topics of the project with an overview of all steps
taken, and how to access those informations.

Interacting with API
--------------------

The developed API is actually on high now at my particular App Engine on Google Cloud, therefore
this API was developed as a microservice to attend the design of App Engine. After developing and
training the model to predict product categories, this model was uploaded with the API source code
to App Engine as a `joblib` dump. This particular model, is one with such confidence:

.. image:: _static/confidence.png
   :align: center
   :width: 600

To access the API, you can use the following end-point:

.. code-block::

   https://classify-data-dot-elo7interview.rj.r.appspot.com/v1/categorize

.. note:: 

   If the provided URL does not work, please contact me to start again the service.


The API expects an POST request with a body such as in the following example:

.. code-block:: json

   {
    "products": [
        {
            "product_id": 11394449,
            "seller_id": 8324141,
            "query": "espirito santo",
            "search_page": 2,
            "position": 6,
            "title": "Mandala Esp\u00edrito Santo",
            "concatenated_tags": "mandala mdf",
            "creation_date": "14/11/2015",
            "price": 171.89,
            "weight": 1200.0,
            "express_delivery": 1,
            "minimum_quantity": 4,
            "view_counts": 244,
            "order_counts": 0.0
        },
        {
            "product_id": 15534262,
            "seller_id": 6939286,
            "query": "cartao de visita",
            "search_page": 2,
            "position": 0,
            "title": "Cart\u00e3o de Visita",
            "concatenated_tags": "cartao visita panfletos tag adesivos copos long drink canecas",
            "creation_date": "4/4/2018",
            "price": 77.67,
            "weight": 8.0,
            "express_delivery": 1,
            "minimum_quantity": 5,
            "view_counts": 124,
            "order_counts": 0.0
        }
      ]
   }

And you should expected an output like:

.. code-block:: json

   {
    "categories": [
        "Decoração",
        "Papel e Cia"
      ]
   }


.. toctree::
   :maxdepth: 3
   :caption: Machine Learning Model

   model


.. toctree::
   :maxdepth: 3
   :caption: Code Documentation

   modules


.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
