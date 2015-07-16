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

import json

from .ntokloapi import NtokloAPIBase
from .config import DEFAULT_UV
from .exceptions import RequestError


class Event(NtokloAPIBase):

    def send(self, payload, version=DEFAULT_UV):

        """Create a new event on the API.

        An event is some action related to a user from your platform that
        accesed one of your recommendations.

        Args:
            payload: Universal Value object (in JSON format) to be passed to
                     the API.
            version: (**optional**) Which version of the UV to use, the default
                     is the latest one used by the ntoklo API.

        Raises:
            RequestError: In case the request couldn't be made or failed.

        Returns:
            String: Status code of the request. `204 No Content` is the
                    expected response.

        .. versionadded:: 0.1
        """
        method = "POST"
        uri = "/event"
        url = "{}{}".format(self.api_endpoint, uri)
        auth_token = self.get_token(uri, method)
        self.headers['Authorization'] = auth_token

        if 'version' not in payload:
            # The version didn't come through the UV. We need to add it.
            payload['version'] = version
        try:
            r = self.session.post(url, data=json.dumps(payload),
                                  headers=self.headers)
            return r.status_code
        except Exception as e:
            raise RequestError(e)
