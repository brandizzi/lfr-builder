#!/usr/bin/env python
#
# Copyright 2015 Adam Victor Brandizzi
#
# This file is part of Liferay Builder.
#
# Liferay Builder is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Liferay Builder is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Liferay Builder.  If not, see <http://www.gnu.org/licenses/>.

import unittest
try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

from lfrbuilder.properties import Properties

class TestProperties(unittest.TestCase):
    """
    Test for a class that parses and edits properties files.
    """

    def test_get_property(self):
        """
        ``Properties`` receives a file-like object and reads a property
        from it.
        """
        stream = StringIO.StringIO("test.property=value")
        props = Properties(stream)

        self.assertEquals('value', props['test.property'])

    def test_set_property(self):
        """
        ``Properties`` should be able to update its properties (but it is
        not persited back into the file).
        """
        stream = StringIO.StringIO("test.property=value")
        props = Properties(stream)
        props['test.property'] = 'example'

        self.assertEquals('example', props['test.property'])

    def test_to_string(self):
        """
        ``Properties.__str__()`` should return a string value suitable to be
        written in a properties file.
        """
        stream = StringIO.StringIO("test.property=value")
        props = Properties(stream)
        props['test.property'] = 'example'

        self.assertEquals('test.property=example', str(props))
