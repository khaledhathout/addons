# -*- encoding: utf-8 -*-

{
    'name': 'Odoo 15 Account Bank Statement Import',
<<<<<<< HEAD
<<<<<<< HEAD
    'version': '15.0.2.4.0',
=======
    'version': '15.0.2.1.0',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
=======
    'version': '15.0.2.1.0',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
    'category': 'Accounting',
    'depends': ['account'],
    'website': 'https://www.odoomates.tech',
    'author': 'Odoo Mates, Odoo SA',
    'support': 'odoomates@gmail.com',
    'maintainer': 'Odoo Mates',
    'license': 'LGPL-3',
    'description': """Generic Wizard to Import Bank Statements In Odoo15 Community Edition.
(This module does include any CSV and XLSX type import format.)""",
    'data': [
        'security/ir.model.access.csv',
        'wizard/journal_creation.xml',
        'views/account_bank_statement_import_view.xml',
<<<<<<< HEAD
<<<<<<< HEAD
=======
        # 'views/res_config_settings_views.xml',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
=======
        # 'views/res_config_settings_views.xml',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
    ],
    'demo': [
        'demo/partner_bank.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': True,
}
