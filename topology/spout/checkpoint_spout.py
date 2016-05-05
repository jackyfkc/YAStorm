from topology.spout import interfaces


class CheckpointSpout(interfaces.ISpout):
    """ Emits checkpoint tuples which is used to save the state across the
    topology. If a topology contains stateful bolts, CheckpointSpout are
    automatically added to the topology. There is only one Checkpoint task
    per topology.
    """
    pass  # TODO


class CheckPointState(object):
    class State(object):
        COMMITTED, COMMITTING, PREPARING = 0, 1, 2

    class Action(object):
        PREPARE, COMMIT, ROLLBACK, INITSTATE = 0, 1, 2, 3

    def __init__(self, txid, state):
        self._txid = txid
        self._state = state

    def next_state(self):
        pass

    def __hash__(self):
        result = self._txid ^ (self._txid >> 32)
        result = 31 * result + hash(self._state) if self._state else 0
        return result
