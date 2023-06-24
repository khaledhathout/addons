# -*- coding: utf-8 -*-

{
    'name': 'Odoo 15 Accounting Financial Reports',
<<<<<<< HEAD
<<<<<<< HEAD
    'version': '15.0.8.2.0',
=======
    'version': '15.0.8.0.0',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
=======
    'version': '15.0.8.0.0',
>>>>>>> 358f758393aa199c8d4488b4302b70097eab143b
    'category': 'Invoicing Management',
    'description': 'Accounting Reports For Odoo 15, Accounting Financial Reports, '
                   'Odoo 15 Financial Reports',
    'summary': 'Accounting Reports For Odoo 15',
    'sequence': '1',
    'author': 'Odoo Mates, Odoo SA',
    'license': 'LGPL-3',
    'company': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'support': 'odoomates@gmail.com',
    'website': 'https://www.youtube.com/watch?v=yA4NLwOLZms',
    'depends': ['account'],
    'live_test_url': 'https://www.youtube.com/watch?v=yA4NLwOLZms',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/financial_report.xml',
        'views/settings.xml',
        'wizard/partner_ledger.xml',
        'wizard/general_ledger.xml',
        'wizard/trial_balance.xml',
        'wizard/balance_sheet.xml',
        'wizard/profit_and_loss.xml',
        'wizard/tax_report.xml',
        'wizard/aged_partner.xml',
        'wizard/journal_audit.xml',
        'report/report.xml',
        'report/report_partner_ledger.xml',
        'report/report_general_ledger.xml',
        'report/report_trial_balance.xml',
        'report/report_financial.xml',
        'report/report_tax.xml',
        'report/report_aged_partner.xml',
        'report/report_journal_audit.xml',
        'report/report_journal_entries.xml',
    ],
    'pre_init_hook': '_pre_init_clean_m2m_models',
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': ['static/description/banner.gif'],
}
