{
    'name': 'POS Receipt Hide Odoo Branding',
    'version': '19.0.1.0.0',
    'category': 'Point of Sale',
    'summary': 'Hide Odoo branding from POS receipt',
    'author': 'Athman',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_receipt_hide_odoo_branding/static/src/js/pos_config_refresh.js',
            'pos_receipt_hide_odoo_branding/static/src/xml/order_receipt.xml',
        ],
    },
    'installable': True,
}
