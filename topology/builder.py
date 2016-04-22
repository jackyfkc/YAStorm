# -*- coding: utf-8 -*-


class TopologyBuilder(object):
    def __init__(self):
        self._spouts = {}
        self._bolts = {}
        self._commons = {}

        self._has_stateful_bolt = False

    def create_topology(self):
        pass

    def set_bolt(self, cid, bolt, parallelism_hint=None):
        """

        :param cid: The id of this component
        :param bolt: The bolt
        :return:
        """
        pass  # TODO

    def set_spout(self, cid, spout, parallelism_hint=None):
        pass  # TODO
