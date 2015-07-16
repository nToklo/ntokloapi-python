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
from collections import OrderedDict
try:
    # Try to load first the Python 3 version
    from urllib.parse import urlencode
except:
    # Fallback to Python 2
    from urllib import urlencode

from .ntokloapi import NtokloAPIBase
from .exceptions import RequestError


class Recommendation(NtokloAPIBase):

    def _clean_querystring(self, querystring):
        for key in querystring:
            if not querystring[key]:
                del querystring[key]
        return querystring

    def get(self, userid='', productid='', scope='', value=''):

        """Request the recommendations for the application.

        Args:
            userid (str): (**optional**) the user ID number from your
                          application.
            productid (str): (**optional**) The product ID number from your
                             application.
            scope (str): (**optional**) A product attribute for which to scope
                         recommendations. For example scope=category will
                         consider the product category when returning
                         recommendations. Supports: category, manufacturer,
                         vendor, action.
            value (str): (**optional**) The value for the recommendation scope.
                         For example scope=category&value=shoes will consider
                         the shoe category when returning recommendations.
                         The value parameter can be any string value.

        Raises:
            RequestError: In case the request couldn't be made or failed.

        Returns:
            JSON Object: A JSON object with the recommendation as "items" and
                         a "tracker_id"

        .. versionadded:: 0.1
        """
        method = "GET"
        uri = "/recommendation"
        url = "{}{}".format(self.api_endpoint, uri)
        qs_values = self._clean_querystring(OrderedDict(userId=userid,
                                                        productId=productid,
                                                        scope=scope,
                                                        value=value))
        querystring = urlencode(qs_values)
        auth_token = self.get_token(uri + "?" + querystring, method)
        self.headers['Authorization'] = auth_token

        try:
            r = self.session.get(url, params=querystring, headers=self.headers)
            return json.loads(r.text)
        except Exception as e:
            raise RequestError(e)
