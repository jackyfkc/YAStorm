# -*- coding: utf-8 -*-

DEFAULT_STREAM_ID = 'default'


class SpoutOutputCollector(object):
    def __init__(self, delegate):
        self._delegate = delegate

    def emit(self, stream_id, tuple, message_id=None):
        """ Emits a new tuple to the specified output stream with the given
        message id. When Storm detects that this tuple has been fully
        processed or has failed to be fully processed, the spout will
        receive an ack or fail callback respectively with the message_id as
        long as the message id was not null. If the message_id was null,
        Storm will not track the tuple and no callback will be received.
        The emitted values must be immutable.

        :param stream_id: output stream, if it is null, the tuple will be
                emitted to the default stream
        :param tuple:
        :param message_id:
        :return: Void
        """
        if stream_id is None:
            stream_id = DEFAULT_STREAM_ID
        self._delegate.emit(stream_id, tuple, message_id)

    def emit_direct(self, task_id, stream_id, tuple, message_id=None):
        """ Emit a tuple to the specified task on the specified output stream.
        This output stream must have been declared as a direct stream, and the
        specified task must use a direct grouping on this stream to receive
        the message. The emitted values must be immutable.

        If no message id is specified, Storm will not track this tuple so ack
        and fail will never be called for this tuple

        :param task_id:
        :param stream_id: output stream, if it is null, the tuple will be
                emitted to the default stream
        :param tuple:
        :param message_id:
        :return: Void
        """
        if stream_id is None:
            stream_id = DEFAULT_STREAM_ID
        self._delegate.emit_direct(task_id, stream_id, tuple, message_id)

    def report_error(self, error):
        self._delegate.report_error(error)

    def get_pending_count(self):
        return self._delegate.get_pending_count()
