# -*- coding: utf-8 -*-
"""
Refers to Apache Storm, storm/storm-core/src/jvm/org/apache/storm/task/
"""


class IBolt(object):
    def prepare(self, storm_conf, context, collector):
        """ It provides the bolt with the environment in which
        the bolt executes. Called when a task for this component is initialized
        within a worker on the cluster.

        :param storm_conf: The storm configuration for this bolt
        :param context: This object can be used to get information about this
               task's place within the topology, including the task id and
               component id of this task, input and output information, etc.
        :param collector: The collector is used to emit tuples from this bolt.
               Tuples can be emitted at any time, including the prepare and
               cleanup methods. The collector is thread-safe and should be
               saved as an instance variable of this bolt object.
        :return: Void
        """
        raise NotImplementedError()

    def execute(self, input):
        """ Process a single tuple of input

        :param input: The input tuple to be processed
        :return: Void
        """
        raise NotImplementedError()

    def cleanup(self):
        """ Called when an IBolt is going to be shutdown. There is no guarantee
            that the cleanup will be called, because the supervisor kill -9's
            worker processes on the cluster

        :return: Void
        """
        raise NotImplementedError()
