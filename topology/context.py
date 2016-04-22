# -*- coding: utf-8 -*-


class TopologyContext(object):
    """ A given `TopologyContext` is given to bolts and spouts in their
        `prepare()` and `open()`, respectively. This object provides
        information about the component's place within the topology, such as
        task ids, inputs and outputs, etc.
    """
    def __init__(self, topology, conf, task_to_component):
        # TODO
        raise NotImplementedError()
