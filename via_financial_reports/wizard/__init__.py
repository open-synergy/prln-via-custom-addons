###############################################################################
#
#  Vikasa Infinity Anugrah, PT
#  Copyright (C) 2012 Vikasa Infinity Anugrah <http://www.infi-nity.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as
#  published by the Free Software Foundation, either version 3 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see http://www.gnu.org/licenses/.
#
###############################################################################

import os
import glob

_mod_dir = os.path.abspath(os.path.dirname(__file__))
_mod_search_paths = [_mod_dir]
for mod_name in filter(lambda mod_name: mod_name != '__init__',
                       map(lambda file_path: os.path.basename(file_path)[:-3],
                           glob.glob(os.path.join(_mod_dir, '*.py')))):
    __import__(__package__ + '.' + mod_name)
