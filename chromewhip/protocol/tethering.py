# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import target as Target

class Tethering(PayloadMixin):
    """ The Tethering domain defines methods and events for browser port binding.
    """
    @classmethod
    def bind(cls,
             port: Union['int'],
             ):
        """Request browser port binding.
        :param port: Port number to bind.
        :type port: int
        """
        return (
            cls.build_send_payload("bind", {
                "port": port,
            }),
            None
        )

    @classmethod
    def unbind(cls,
               port: Union['int'],
               ):
        """Request browser port unbinding.
        :param port: Port number to unbind.
        :type port: int
        """
        return (
            cls.build_send_payload("unbind", {
                "port": port,
            }),
            None
        )



class AcceptedEvent(BaseEvent):

    js_name = 'Tethering.accepted'
    hashable = ['connectionId']
    is_hashable = True

    def __init__(self,
                 port: Union['int', dict],
                 connectionId: Union['str', dict],
                 ):
        if isinstance(port, dict):
            port = int(**port)
        self.port = port
        if isinstance(connectionId, dict):
            connectionId = str(**connectionId)
        self.connectionId = connectionId

    @classmethod
    def build_hash(cls, connectionId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
