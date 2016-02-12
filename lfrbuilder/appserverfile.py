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

import getpass
import os.path

from lfrbuilder.log import log, debug

@log
def set_property(
        key, value, repository='.', user_name=None, base_file_name='app.server',
        extension_file_name='properties'
    ):
    if user_name is None:
        user_name = getpass.getuser()

    file_name = '.'.join((base_file_name, user_name, extension_file_name))
    file_path = os.path.join(repository, file_name)
    as_property = ''.join((key, '=', value, '\n'))

    debug('Setting {p} at {f}'.format(p=as_property, f=file_path))

    with open(file_path, 'w') as as_file:
        as_file.write(as_property)

@log
def get_property(
        key, repository='.', user_name=None, base_file_name='app.server',
        extension_file_name='properties'
    ):
    file_name = '.'.join([base_file_name, user_name, extension_file_name])
    file_path = os.path.join([repository, file_name])

    with open(file_path) as as_file:
        for line in as_file:
            k, v = line.split('=')
            if k == key:
                return v
    
