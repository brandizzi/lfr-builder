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

import sys

import decorator

@decorator.decorator
def log(f, *args, **kwargs):
    call_message = 'DEBUG {name} - Calling {name} with {args}, {kwargs}'
    print(call_message.format(name=f.__name__, args=args, kwargs=kwargs))

    result = f(*args, **kwargs)

    if result is not None:
        result_message = 'DEBUG {name} - Result: {result}'
        print(result_message.format(name=f.__name__, result=result))

    return result

def debug(message):
    func_name = sys._getframe(1).f_code.co_name
    
    print('DEBUG {name} - {message}'.format(name=func_name, message=message))
