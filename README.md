Writting...


# PStorm

A lightweight version of [Apache Storm](http://storm.apache.org/), purely written in Python;
The primary reason of implementing this project is to make learning Storm much eaiser. The
implementations refers to Apache Storm v1.0.0.

You can treat this project as a prototype system for Apache Storm.


Architecture
============
<pre>
                                        +--------------------+
                                        | Supervisor: Worker |
                   +------------+     / +--------------------+
                   |  Zookeeper | ----
                   +------------+
+---------+        +------------+       +--------------------+
| Nimbus  | ---->  |  Zookeeper | ----  | Supervisor: Worker |
+---------+        +------------+       +--------------------+
                   +------------+
                   |  Zookeeper | ----  +--------------------+
                   +------------+     \ | Supervisor: Worker |
                                        +--------------------+
</pre>

Nimbus and Supervisor are fail-fast and stateless, and their state is kept in Zookeeper or on
local disk(s).

Nimbus
------
In Apache Storm, Nimbus plays a similar role as the `Job Tracker` in Hadoop.
Nimbus is an Thrift service implemented by [Thriftpy](https://thriftpy.readthedocs.org/en/latest/)


Supervisor
----------
The supervisor runs on each node. It receives assignments from Nimbus and then assign them to workers.
It also monitors the health of the workers and respawns them if necessary.


Internals
---------

**Acker**
https://github.com/apache/storm/blob/v1.0.0/storm-core/src/clj/org/apache/storm/daemon/acker.clj


References
----------
+ [Storm Concepts](http://storm.apache.org/releases/1.0.0/Concepts.html)
+ [Storm Code Structure](http://storm.apache.org/releases/1.0.0/Structure-of-the-codebase.html)
+ Storm - Distributed and fault-tolerant realtime computation, Nathan Marz
+ Storm @ Twitter
