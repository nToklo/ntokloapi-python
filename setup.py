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

from distutils.core import setup
from setuptools import find_packages

from . import __version__

setup(
    name='ntokloapi-python',
    version=__version__,
    author=u'Oscar Carballal Prego',
    author_email='oscar.carballal@ntoklo.com',
    packages=find_packages(),
    url='http://bitbucket.org/bruno/django-geoportail',
    license='BSD licence, see LICENCE.txt',
    description='Add maps and photos from the French National Geographic' + \
                ' Institute to GeoDjango',
    long_description=open('README.txt').read(),
    zip_safe=False,
)


