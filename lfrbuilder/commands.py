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

import os.path

import baker

from lfrbuilder.dir import change_dir
from lfrbuilder.appserverfile import get_property
from lfrbuilder.build import build as lfrbuild

@baker.command
def build(repository='.', bundle=None, branch=None):
    repository=os.path.expanduser(repository)

    if bundle is None:
        bundle = get_property('app.server.parent.dir')
    else:
        bundle = os.path.expanduser(bundle)

    with change_dir(repository):
        lfrbuild(
            repository=repository,
            bundle=bundle,
            branch=branch
        )

