class ITuple(object):
    def get_source_global_stream_id(self):
        """ returns the global stream id (component + stream) of this tuple

        :return: GlobalStreamId
        """
        raise NotImplementedError()

    def get_source_component(self):
        """ gets the id of the component that created this tuple

        :return: string
        """
        raise NotImplementedError()

    def get_source_task(self):
        """ gets the id of the task that created this tuple

        :return: int
        """
        raise NotImplementedError()

    def get_source_stream_id(self):
        """ get the id of the stream that this tuple was emitted to

        :return: int
        """
        raise NotImplementedError()

    def get_message_id(self):
        """ gets the message id that associated with this tuple

        :return: int
        """
        raise NotImplementedError()
