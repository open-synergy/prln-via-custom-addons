# -*- encoding: utf-8 -*-
##############################################################################
#
#    Vikasa Infinity Anugrah, PT
#    Copyright (c) 2011 - 2012 Vikasa Infinity Anugrah <http://www.infi-nity.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "VIA Reporting Utility",
    "version": "1.0",
    "author": "Vikasa Infinity Anugrah, PT",
    "category": "VIA/Reporting",
    "description": """
    This module provides a set of reporting utilities for VIA reporting modules.
    """,
    "website": "http://www.infi-nity.com",
    "license": "GPL-3",
    "depends": [
        "base",
        "stock",
    ],
    "init_xml": [],
    'update_xml': [
        'security/ir.model.access.csv',
        'oerp_report_framework.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
