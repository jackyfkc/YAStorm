Internals
---------
+ [xor vs reference counting]
(https://groups.google.com/forum/#!searchin/storm-user/nathan$20marz/storm-user/pw2P8J0U9CQ/qJhZ96sMlH4J)
+ [What happened when multiple bolts reading the same stream?]
(https://groups.google.com/forum/#!searchin/storm-user/nathan$20marz/storm-user/qbbngzKQ0a0/dLc5MZhkT00J)
Each bolt will get its own copy of that tuple, and each tuple is completely independent.
Each bolt should ack their tuple

Usage
-----
+ [How to handle multiple streams](https://groups.google.com/forum/#!topic/storm-user/gNt00aUUUw4)



Spout
-----
https://groups.google.com/forum/#!searchin/storm-user/nathan$20marz/storm-user/SLxW62kgKqc/PNRlR1ajBFkJ

