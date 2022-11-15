## begin license ##
#
# "Autotest": a simpler test runner for python
#
# Copyright (C) 2022 Seecr (Seek You Too B.V.) https://seecr.nl
#
# This file is part of "Autotest"
#
# "Autotest" is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# "Autotest" is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with "Autotest".  If not, see <http://www.gnu.org/licenses/>.
#
## end license ##


""" this should be a hook, so you can get a mock by:

    m = test.mock_object(...)

    Doing so keeps test the only API access point.
"""

# helpers
def mock_object(*functions, **more):
    """ Creates an object from a bunch of functions.
        Useful for testing methods from inside the class definition. """
    self = mock.Mock()
    self.configure_mock(**{f.__name__: types.MethodType(f, self) for f in functions}, **more)
    return self



