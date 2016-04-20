class Tuple(object):
    def getSourceGlobalStreamId(self):
        """ Returns the global stream id (component + stream) of this tuple

        :return: GlobalStreamId
        """
        pass

    def getSourceComponent(self):
        """ Gets the id of the component that created this tuple

        :return: String
        """
        pass

    def getSourceTask(self):
        """ Gets the id of the task that created this tuple

        :return: int
        """
        pass

    def getSourceStreamId(self):
        """ Get the id of the stream that this tuple was emitted to

        :return:
        """
        pass

    def getMessageId(self):
        """ Gets the message id that associated with this tuple

        :return:
        """
        pass
