# PStorm

A lightweight version of [Apache Storm](http://storm.apache.org/), purely written in Python, just for fun!

Refers to Apache Storm v1.0.0


Architecture
============
                                        +---------+
                                        | Worker  |
                   +------------+     / +---------+
                   |  Zookeeper | ----
                   +------------+
+---------+        +------------+       +---------+
| Nimbus  | ---->  |  Zookeeper | ----  | Worker  |
+---------+        +------------+       +---------+
                   +------------+
                   |  Zookeeper | ----  +---------+
                   +------------+     \ | Worker  |
                                        +---------+

Nimbus
------
In Apache Storm, Nimbus plays a similar role as the `Job Tracker` in Hadoop.
Nimbus is an Thrift service implemented by [Thriftpy](https://thriftpy.readthedocs.org/en/latest/)


Supervisor
----------
The supervisor runs on each node. It receives assignments from Nimbus and assign them to workers.


Internals
---------

**Acker**
https://github.com/apache/storm/blob/v1.0.0/storm-core/src/clj/org/apache/storm/daemon/acker.clj

** Apache Storm Code Structure **
http://storm.apache.org/releases/1.0.0/Structure-of-the-codebase.html


References
----------
[Apache Storm Homepage](http://storm.apache.org/)
Storm - Distributed and fault-tolerant realtime computation, Nathan Marz
