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


class IncorrectHTTPMethod(Exception):

    """A non accepted HTTP method has been used for the request.

    Example:
        Accepted methods are GET and POST but function receives PUT.
    """
    def __init__(self, value):
        self.value = "The HTTP method {} is not allowed.".format(value)

    def __str__(self):
        return repr(self.value)


class SignatureGenerationError(Exception):

    """Throw this error whenever the signature creation has failed.

    Example:
        The hmac module couldn't generate the signature due to a malformed URI.
    """
    def __init__(self, value):
        self.value = "Couldn't generate the signature for the request. Error was: {}".format(value)

    def __str__(self):
        return repr(self.value)


class IncorrectPythonVersion(Exception):

    """Throw this error whenever the signature creation has failed.

    Example:
        The hmac module couldn't generate the signature due to a malformed URI.
    """
    def __init__(self, value):
        self.value = "Python versions < 2.7.x are not supported."

    def __str__(self):
        return repr(self.value)


class RequestError(Exception):

    """Throw this error whenever a request fails. Instead of letting python
    requests throw its own error, we capture it and show it on our own
    exception.

    Example:
        Try to POST or GET a URL and have a connection error, tiemout, etc.
    """
    def __init__(self, value):
        self.value = "There has been an error with the request: {}".format(value)

    def __str__(self):
        return repr(self.value)
