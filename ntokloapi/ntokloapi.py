# Copyright 2015 nToklo Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import hmac
from hashlib import sha1

import requests

from .exceptions import IncorrectHTTPMethod, SignatureGenerationError
from .config import ACCEPTED_METHODS, REALM


class NtokloAPIBase():

    """Base class of the nToklo API connector

    This class will take care of authentication and exceptions of the API,
    retuning the required codes to the functions that use it. It will also open
    a requests session against the API to retry in case the API connection
    fails.

    Args:
        key (str): The user private API key. It can be obtained from the nToklo
             console.
        secret (str): The user private API secret. It can be obtained from the nToklo
                console.
        protocol (str): (**optional**) The protocol over to which connnect to the API. Default:
                  https://

    .. versionadded:: 0.1
    """

    def __init__(self, key, secret, protocol="https://"):
        self.key = key
        self.secret = secret
        self.api_endpoint = "{}api.ntoklo.com".format(protocol)

        # Define base headers
        self.headers = {'Content-Type': 'application/json; charset=utf-8'}
        # Open a foolproof request session
        self.session = requests.Session()
        self.session.mount(protocol, requests.adapters.HTTPAdapter(max_retries=3))

    def get_token(self, uri, http_method):

        """Get the required signature to sign the request.

        Please check http://docs.ntoklo.com/start.php/authentication for more
        information.

        Args:
            uri (str): The URI of the API resource
            http_method (str): HTTP method with which make the request.

        Raises:
            SignatureGenerationError: The signature didn't match (URL of the
                                      request and the URL signed)
            IncorrectHTTPMethod: The method is not allowed in the API.

        Returns:
            String: String containing a signed token.
        """
        if http_method in ACCEPTED_METHODS:
            request_str = "{}&{}{}".format(http_method, self.api_endpoint, uri).encode("utf-8")
            sha1_key = "{}&{}".format(self.key, self.secret).encode("utf-8")
            try:
                signature = hmac.new(bytearray(sha1_key),
                                     request_str, sha1).hexdigest()
                auth_header = "{} {}:{}".format(REALM, self.key, signature)
            except Exception as e:
                raise SignatureGenerationError(e)
        else:
            raise IncorrectHTTPMethod(http_method)

        return auth_header
