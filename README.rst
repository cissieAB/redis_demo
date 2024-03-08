Demo: Using `Redis Streams <https://redis.io/docs/data-types/streams/>`_ as the Backend
=======================================================================================

Redis operations
----------------

1. Install Redis.

.. code:: bash

    $ sudo yum install redis

2. Start the redis server.

.. code:: bash

    $ redis-server &  # start in the backend
    1103496:C 07 Mar 2024 20:47:04.288 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo   

3. Ping the Redis server

.. code:: bash

    $ redis-cli ping
    PONG

4. Some `redis-cli` commands

::

    $ redis-cli
    127.0.0.1:6379> XLEN ejfat   # check the length of "ejfat" stream
    127.0.0.1:6379> XRANGE ejfat - + COUNT 1   # check the first message of "ejfat"
    127.0.0.1:6379> XREVRANGE ejfat + - COUNT 1  # check the last message
    # Block for 10 milliseconds and read only the new message in the stream "ejfat". Similar to `tail -f`
    127.0.0.1:6379> XREAD BLOCK 10 STREAMS ejfat $
    127.0.0.1:6379> XGROUP CREATE ejfat daos $   # create a usergroup "daos" for stream "ejfat"


Refs
~~~~
- Official Redis Streams documentation: `Introduction to Redis streams <https://redis.io/docs/data-types/streams/>`_

Python Redis+DAOS client demo
-----------------------------

One Python program reads the `tmpfile` and write to a Redis Stream by chunks. Another program reads from the Redis
Stream and save the content to DAOS containers.

Setting the Conda Python environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    conda env create --name daos_test python=3.10
    conda activate daos_test

    # Install Redis client
    conda install -n daos_test redis-py


Other docs

* `Build DAOS from scratch on daosfs05 <./daos_install.rst>`_
