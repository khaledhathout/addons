# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Odoo 15 Recurring Payment',
    'author': 'Odoo Mates',
    'category': 'Accounting',
<<<<<<< HEAD
<<<<<<< HEAD
    'version': '1.6.0',
=======
    'version': '1.4.0',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
=======
    'version': '1.4.0',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
    'description': """Odoo 15 Recurring Payment, Recurring Payment In Odoo, Odoo 15 Accounting""",
    'summary': 'Use recurring payments to handle periodically repeated payments',
    'sequence': 11,
    'website': 'https://www.odoomates.tech',
    'depends': ['account'],
    'license': 'LGPL-3',
    'data': [
        'data/sequence.xml',
        'data/recurring_cron.xml',
        'security/ir.model.access.csv',
        'views/recurring_template_view.xml',
        'views/recurring_payment_view.xml'
    ],
    'images': ['static/description/banner.png'],
}
