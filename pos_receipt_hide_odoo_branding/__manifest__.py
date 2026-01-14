{
    'name': 'POS Receipt Hide Odoo Branding',
    'version': '19.0.2.0.0',
    'category': 'Point of Sale',
    'summary': 'Hide "Powered by Odoo" branding from POS receipts',
    'description': """
This module hides the "Powered by Odoo" branding from Point of Sale receipts.

Features:
- Automatically hides Odoo branding on all POS receipts
- No configuration needed - install and it works
- Compatible with Odoo Import Module (ZIP installation)

Installation:
1. Go to Apps > Import Module (developer mode required)
2. Upload the ZIP file
3. The branding will be hidden automatically
    """,
    'author': 'Athman',
    'license': 'LGPL-3',
    'depends': ['point_of_sale', 'base_import_module'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_receipt_hide_odoo_branding/static/src/xml/order_receipt.xml',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}
