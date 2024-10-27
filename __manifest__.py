{
    'name': 'POS Order List',
    'version': '1.0',
    'category': 'Point of Sale',
    'summary': 'Display a list of POS orders with their status',
    'description': """
        This module adds a menu item to display a list of Point of Sale orders
        with their current status.
    """,
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_order_list_views.xml',
        'views/pos_order_list_menus.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
