# -*- coding: utf-8 -*-
{
    'name': "multi_recipient_notification",

    'summary': """
        Allow sending emails to multiple recipients at once""",

    'description': """
        This module will result in recipients of notification emails in Odoo to see which other recipients
        the email has been sent to. When one of the recipient replies, Odoo will not notify the followers by itself
        anymore, instead relying on the more traditional way of how sending emails and receiving replies works.
    """,

    'author': "Daniel Salimian, Monday Merch",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'portal'],

}
