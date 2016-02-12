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

import contextlib
import glob
import os
import os.path
import shutil
import tempfile

@contextlib.contextmanager
def change_dir(path):
    previous_dir = os.getcwd()
    new_dir = os.path.expanduser(path)
    os.chdir(new_dir)
    yield
    os.chdir(previous_dir)

@contextlib.contextmanager
def temp_dir(path):
    if path is None:
        path = tempfile.mkdtemp()
        yield path
        shutil.rmtree(path)
    else:
        yield path

def copy_files(src, dst, pattern='portal*.properties'):
    with change_dir(src):
        for pf in glob.glob(pattern):
            shutil.copy(pf, dst)
            shutil.copy(pfile, temp_bundle)

def replace_tree(src, dst):
    if os.path.exists(dst) and os.path.isdir(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
