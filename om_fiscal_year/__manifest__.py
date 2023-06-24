# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo 15 Fiscal Year & Lock Date',
<<<<<<< HEAD
<<<<<<< HEAD
    'version': '2.2.0',
=======
    'version': '2.1.0',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
=======
    'version': '2.1.0',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
    'category': 'Accounting',
    'summary': 'Odoo 15 Fiscal Year, Fiscal Year in Odoo 15, Lock Date in Odoo 15',
    'description': 'Odoo 15 Fiscal Year, Fiscal Year in Odoo 15',
    'live_test_url': 'https://www.youtube.com/watch?v=Kj4hR7_uNs4',
    'sequence': '1',
    'website': 'https://www.odoomates.tech',
    'author': 'Odoo Mates, Odoo SA',
    'maintainer': 'Odoo Mates',
    'license': 'LGPL-3',
    'support': 'odoomates@gmail.com',
    'depends': ['account'],
<<<<<<< HEAD
<<<<<<< HEAD
    'excludes': ['account_accountant'],
=======
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
=======
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'security/account_security.xml',
        'wizard/change_lock_date.xml',
        'views/fiscal_year.xml',
        'views/settings.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/banner.png'],
}
