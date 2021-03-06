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


class DictList(dict):

    """Create lists inside dictionaries with duplicate keys.

    Args:
        dict (dict): A dictionary with keys and values

    Raises:
        KeyError: If the key if malformed

    Returns:
        Dictionary: Reordered dictionary in which the same keys joined into
                    a list.

    References:
        StackOverflow: http://stackoverflow.com/a/10665285
    """
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(DictList, self).__setitem__(key, [])
        self[key].append(value)
