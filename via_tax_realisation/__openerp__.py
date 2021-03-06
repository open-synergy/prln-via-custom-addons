# -*- encoding: utf-8 -*-
##############################################################################
#
#    Vikasa Infinity Anugrah, PT
#    Copyright (c) 2011 - 2013 Vikasa Infinity Anugrah <http://www.infi-nity.com>
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
    'name': 'VIA Tax Realisation',
    'version': '1.1',
    'category': 'Accounting & Finance',
    #'sequence': 19,
    'complexity': 'normal',
    'description': """
    This module provide the functionality to create realisation journal from each
    tax entry in invoice or refund.

    To make this module work, realisation accounts and journals for invoice and
    refunds must be defined for each tax related account.
    """,
    'author': 'Vikasa Infinity Anugrah, PT',
    'website': 'http://www.infi-nity.com',
    #'images' : ['images/purchase_order.jpeg', 'images/purchase_analysis.jpeg', 'images/request_for_quotation.jpeg'],
    'depends': [
        'via_account_taxform',
        'via_partner_enhancements',
    ],
    'data': [
        'wizard/view_WizardTaxRealisation.xml',
        'wizard/view_WizardCreateTaxformRealisation.xml',
        'view/view_AccountAccount.xml',
        'view/view_AccountInvoice.xml',
    ],
    'test': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    #'certificate': '0057234283549',
    'application': False,

}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
