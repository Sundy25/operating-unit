# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Eficent (<http://www.eficent.com/>)
#              Jordi Ballester Alomar <jordi.ballester@eficent.com>
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    "name": "HR Expense Operating Unit",
    "version": "1.0",
    "license": 'AGPL-3',
    "author": "Eficent",
    "category": "Generic Modules/Human Resources",
    "depends": ["hr_expense", "account_operating_unit"],
    "description": """
HR Expense Operating Unit
=========================
Adds a the operating unit to the HR Expense.
    """,
    "data": [
        "views/hr_expense_view.xml",
        "security/hr_expense_security.xml"
    ],
    'demo': [],
    'test': [
    ],
    'installable': True,
}
