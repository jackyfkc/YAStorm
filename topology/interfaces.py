from spout.interfaces import ISpout
from bolt.interfaces import IBolt


class IComponent(object):
    """ Common methods for all possible components in a topology

    """
    def declare_output_fields(self, declarer):
        """ Declare the output schema, like stream ids, output fields

        :param declarer: OutputFieldsDeclarer
        :return: Void
        """
        pass

    def get_component_configuration(self):
        """ Declare configuration specific to this component

        :return:
        """
        pass


class IRichSpout(ISpout, IComponent):
    pass


class IRichBolt(IBolt, IComponent):
    pass
