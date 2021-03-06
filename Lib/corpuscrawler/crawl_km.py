# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, print_function, unicode_literals
import re
from corpuscrawler.util import crawl_radio_free_asia, crawl_udhr


def crawl(crawler):
    out = crawler.get_output(language='km')
    crawl_udhr(crawler, out, filename='udhr_khm.txt')
    # Khmer RFA does not use Unicode encoding for content before 2008.
    crawl_radio_free_asia(crawler, out, edition='khmer', start_year=2008)
