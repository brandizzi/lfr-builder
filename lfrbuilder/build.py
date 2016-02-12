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

import git
import os

from lfrbuilder.dir import change_dir, temp_dir, copy_files, replace_tree
from lfrbuilder.appserverfile import set_property
from lfrbuilder.log import log

commands = (
    'ant -f build-dist.xml unzip-tomcat',
    'ant all',
    'ant -f build-test.xml setup-testable-tomcat'
)

@log
def clone_repo(repo, path, branch=None):
    clone = repo.clone(path)

    if branch:
        clone.head.reference = branch

    return clone
    

def build(
        repository, bundle, branch=None, temp_repo=None, temp_bundle=None,
        portal_files_glob='portal*.properties', 
        build_commands=commands
    ):
    repo = git.Repo(repository)

    with temp_dir(temp_repo) as clone_path, \
         temp_dir(temp_bundle) as bundle_path:
        clone = clone_repo(repo, clone_path, branch)

        with change_dir(clone_path):
            set_property(
                key='app.server.parent.dir', value=bundle_path,
                repository=clone_path
            )

            for c in build_commands:
                os.system(c)

            if os.path.exists(bundle) and os.path.isdir(bundle):
                copy_files(src=bundle, dst=bundle_path)
            replace_tree(src=bundle_path, dst=bundle)
