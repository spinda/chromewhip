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
from chromewhip.protocol import network as Network
from chromewhip.protocol import io as IO
from chromewhip.protocol import page as Page

# RequestId: Unique request identifier.
RequestId = str

# RequestStage: Stages of the request to handle. Request will intercept before the request issent. Response will intercept after the response is received (but before responsebody is received.
RequestStage = str

# RequestPattern: 
class RequestPattern(ChromeTypeBase):
    def __init__(self,
                 urlPattern: Optional['str'] = None,
                 resourceType: Optional['Network.ResourceType'] = None,
                 requestStage: Optional['RequestStage'] = None,
                 ):

        self.urlPattern = urlPattern
        self.resourceType = resourceType
        self.requestStage = requestStage


# HeaderEntry: Response HTTP header entry
class HeaderEntry(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 value: Union['str'],
                 ):

        self.name = name
        self.value = value


# AuthChallenge: Authorization challenge for HTTP status code 401 or 407.
class AuthChallenge(ChromeTypeBase):
    def __init__(self,
                 origin: Union['str'],
                 scheme: Union['str'],
                 realm: Union['str'],
                 source: Optional['str'] = None,
                 ):

        self.source = source
        self.origin = origin
        self.scheme = scheme
        self.realm = realm


# AuthChallengeResponse: Response to an AuthChallenge.
class AuthChallengeResponse(ChromeTypeBase):
    def __init__(self,
                 response: Union['str'],
                 username: Optional['str'] = None,
                 password: Optional['str'] = None,
                 ):

        self.response = response
        self.username = username
        self.password = password


class Fetch(PayloadMixin):
    """ A domain for letting clients substitute browser's network layer with client code.
    """
    @classmethod
    def disable(cls):
        """Disables the fetch domain.
        """
        return (
            cls.build_send_payload("disable", {
            }),
            None
        )

    @classmethod
    def enable(cls,
               patterns: Optional['[RequestPattern]'] = None,
               handleAuthRequests: Optional['bool'] = None,
               ):
        """Enables issuing of requestPaused events. A request will be paused until client
calls one of failRequest, fulfillRequest or continueRequest/continueWithAuth.
        :param patterns: If specified, only requests matching any of these patterns will produce
fetchRequested event and will be paused until clients response. If not set,
all requests will be affected.
        :type patterns: [RequestPattern]
        :param handleAuthRequests: If true, authRequired events will be issued and requests will be paused
expecting a call to continueWithAuth.
        :type handleAuthRequests: bool
        """
        return (
            cls.build_send_payload("enable", {
                "patterns": patterns,
                "handleAuthRequests": handleAuthRequests,
            }),
            None
        )

    @classmethod
    def failRequest(cls,
                    requestId: Union['RequestId'],
                    errorReason: Union['Network.ErrorReason'],
                    ):
        """Causes the request to fail with specified reason.
        :param requestId: An id the client received in requestPaused event.
        :type requestId: RequestId
        :param errorReason: Causes the request to fail with the given reason.
        :type errorReason: Network.ErrorReason
        """
        return (
            cls.build_send_payload("failRequest", {
                "requestId": requestId,
                "errorReason": errorReason,
            }),
            None
        )

    @classmethod
    def fulfillRequest(cls,
                       requestId: Union['RequestId'],
                       responseCode: Union['int'],
                       responseHeaders: Union['[HeaderEntry]'],
                       body: Optional['str'] = None,
                       responsePhrase: Optional['str'] = None,
                       ):
        """Provides response to the request.
        :param requestId: An id the client received in requestPaused event.
        :type requestId: RequestId
        :param responseCode: An HTTP response code.
        :type responseCode: int
        :param responseHeaders: Response headers.
        :type responseHeaders: [HeaderEntry]
        :param body: A response body.
        :type body: str
        :param responsePhrase: A textual representation of responseCode.
If absent, a standard phrase mathcing responseCode is used.
        :type responsePhrase: str
        """
        return (
            cls.build_send_payload("fulfillRequest", {
                "requestId": requestId,
                "responseCode": responseCode,
                "responseHeaders": responseHeaders,
                "body": body,
                "responsePhrase": responsePhrase,
            }),
            None
        )

    @classmethod
    def continueRequest(cls,
                        requestId: Union['RequestId'],
                        url: Optional['str'] = None,
                        method: Optional['str'] = None,
                        postData: Optional['str'] = None,
                        headers: Optional['[HeaderEntry]'] = None,
                        ):
        """Continues the request, optionally modifying some of its parameters.
        :param requestId: An id the client received in requestPaused event.
        :type requestId: RequestId
        :param url: If set, the request url will be modified in a way that's not observable by page.
        :type url: str
        :param method: If set, the request method is overridden.
        :type method: str
        :param postData: If set, overrides the post data in the request.
        :type postData: str
        :param headers: If set, overrides the request headrts.
        :type headers: [HeaderEntry]
        """
        return (
            cls.build_send_payload("continueRequest", {
                "requestId": requestId,
                "url": url,
                "method": method,
                "postData": postData,
                "headers": headers,
            }),
            None
        )

    @classmethod
    def continueWithAuth(cls,
                         requestId: Union['RequestId'],
                         authChallengeResponse: Union['AuthChallengeResponse'],
                         ):
        """Continues a request supplying authChallengeResponse following authRequired event.
        :param requestId: An id the client received in authRequired event.
        :type requestId: RequestId
        :param authChallengeResponse: Response to  with an authChallenge.
        :type authChallengeResponse: AuthChallengeResponse
        """
        return (
            cls.build_send_payload("continueWithAuth", {
                "requestId": requestId,
                "authChallengeResponse": authChallengeResponse,
            }),
            None
        )

    @classmethod
    def getResponseBody(cls,
                        requestId: Union['RequestId'],
                        ):
        """Causes the body of the response to be received from the server and
returned as a single string. May only be issued for a request that
is paused in the Response stage and is mutually exclusive with
takeResponseBodyForInterceptionAsStream. Calling other methods that
affect the request or disabling fetch domain before body is received
results in an undefined behavior.
        :param requestId: Identifier for the intercepted request to get body for.
        :type requestId: RequestId
        """
        return (
            cls.build_send_payload("getResponseBody", {
                "requestId": requestId,
            }),
            cls.convert_payload({
                "body": {
                    "class": str,
                    "optional": False
                },
                "base64Encoded": {
                    "class": bool,
                    "optional": False
                },
            })
        )

    @classmethod
    def takeResponseBodyAsStream(cls,
                                 requestId: Union['RequestId'],
                                 ):
        """Returns a handle to the stream representing the response body.
The request must be paused in the HeadersReceived stage.
Note that after this command the request can't be continued
as is -- client either needs to cancel it or to provide the
response body.
The stream only supports sequential read, IO.read will fail if the position
is specified.
This method is mutually exclusive with getResponseBody.
Calling other methods that affect the request or disabling fetch
domain before body is received results in an undefined behavior.
        :param requestId: 
        :type requestId: RequestId
        """
        return (
            cls.build_send_payload("takeResponseBodyAsStream", {
                "requestId": requestId,
            }),
            cls.convert_payload({
                "stream": {
                    "class": IO.StreamHandle,
                    "optional": False
                },
            })
        )



class RequestPausedEvent(BaseEvent):

    js_name = 'Fetch.requestPaused'
    hashable = ['requestId', 'frameId', 'networkId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 request: Union['Network.Request', dict],
                 frameId: Union['Page.FrameId', dict],
                 resourceType: Union['Network.ResourceType', dict],
                 responseErrorReason: Union['Network.ErrorReason', dict, None] = None,
                 responseStatusCode: Union['int', dict, None] = None,
                 responseHeaders: Union['[HeaderEntry]', dict, None] = None,
                 networkId: Union['RequestId', dict, None] = None,
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(request, dict):
            request = Network.Request(**request)
        self.request = request
        if isinstance(frameId, dict):
            frameId = Page.FrameId(**frameId)
        self.frameId = frameId
        if isinstance(resourceType, dict):
            resourceType = Network.ResourceType(**resourceType)
        self.resourceType = resourceType
        if isinstance(responseErrorReason, dict):
            responseErrorReason = Network.ErrorReason(**responseErrorReason)
        self.responseErrorReason = responseErrorReason
        if isinstance(responseStatusCode, dict):
            responseStatusCode = int(**responseStatusCode)
        self.responseStatusCode = responseStatusCode
        if isinstance(responseHeaders, dict):
            responseHeaders = [HeaderEntry](**responseHeaders)
        self.responseHeaders = responseHeaders
        if isinstance(networkId, dict):
            networkId = RequestId(**networkId)
        self.networkId = networkId

    @classmethod
    def build_hash(cls, requestId, frameId, networkId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h


class AuthRequiredEvent(BaseEvent):

    js_name = 'Fetch.authRequired'
    hashable = ['requestId', 'frameId']
    is_hashable = True

    def __init__(self,
                 requestId: Union['RequestId', dict],
                 request: Union['Network.Request', dict],
                 frameId: Union['Page.FrameId', dict],
                 resourceType: Union['Network.ResourceType', dict],
                 authChallenge: Union['AuthChallenge', dict],
                 ):
        if isinstance(requestId, dict):
            requestId = RequestId(**requestId)
        self.requestId = requestId
        if isinstance(request, dict):
            request = Network.Request(**request)
        self.request = request
        if isinstance(frameId, dict):
            frameId = Page.FrameId(**frameId)
        self.frameId = frameId
        if isinstance(resourceType, dict):
            resourceType = Network.ResourceType(**resourceType)
        self.resourceType = resourceType
        if isinstance(authChallenge, dict):
            authChallenge = AuthChallenge(**authChallenge)
        self.authChallenge = authChallenge

    @classmethod
    def build_hash(cls, requestId, frameId):
        kwargs = locals()
        kwargs.pop('cls')
        serialized_id_params = ','.join(['='.join([p, str(v)]) for p, v in kwargs.items()])
        h = '{}:{}'.format(cls.js_name, serialized_id_params)
        log.debug('generated hash = %s' % h)
        return h
