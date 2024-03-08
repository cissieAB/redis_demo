Using Redis Stream as the backend
=================================

One Python program reads the `tmpfile` and write to a Redis Stream by chunks. Another program reads from the Redis
Stream and save the content to DAOS containers.

:doc: `daos_install`

- Setting the Conda Python environment.

.. code:: bash

    conda env create --name daos_test python=3.10
    conda activate daos_test

    # Install Redis client
    conda install -n daos_test redis-py
