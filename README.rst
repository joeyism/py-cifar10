
CIFAR 10 Dataset Library
========================

This library was created to allow an easy usage of `CIFAR 10 DATA <https://www.cs.toronto.edu/~kriz/cifar.html>`_. This is a wrapper around the instructions givn on the `CIFAR 10 site <https://www.cs.toronto.edu/~kriz/cifar.html>`_

Installation
------------

.. code-block:: bash

   pip3 install cifar10

Sample Usage
------------

.. code-block:: python

   import cifar10

   for image, label in cifar10.data_batch_generator():
       image # numpy array of an image, which is of shape 32 x 32 x 3
       label # integer value of the image label

API
---

data_batch_generator
^^^^^^^^^^^^^^^^^^^^

Returns a generator of each image and label pair for data batch

.. code-block::

   data_batch_generator(cache_location: str=".") -> Iterator[Tuple[np.array, int]]

parameters
~~~~~~~~~~


* ``cache_location`` (default: library folder location): where to cache the cifar10 data

test_batch_generator
^^^^^^^^^^^^^^^^^^^^

Returns a generator of each image and label pair for test batch

.. code-block::

   test_batch_generator(cache_location: str=".") -> Iterator[Tuple[np.array, int]]

parameters
~~~~~~~~~~


* ``cache_location`` (default: library folder location): where to cache the cifar10 data

meta
^^^^

Returns the raw meta file

.. code-block::

   meta(cache_location: str=".") -> Dict[bytes, Any]

parameters
~~~~~~~~~~


* ``cache_location`` (default: library folder location): where to cache the cifar10 data

image_label_map
^^^^^^^^^^^^^^^

Returns the raw meta file

.. code-block::

   image_label_map(cache_location: str=".") -> Dict[int, str]

parameters
~~~~~~~~~~


* ``cache_location`` (default: library folder location): where to cache the cifar10 data
