# -*- coding: utf-8 -*-
# Copyright 2018 Humanytek - Manuel Marquez <manuel@humanytek.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

{
    'name': 'Add status of sale order invoices to outgoing pickings',
    'version': '9.0.2.0.1',
    'category': 'Stock',
    'author': 'Humanytek',
    'website': "http://www.humanytek.com",
    'license': 'AGPL-3',
    'depends': [
        'stock',
        'sale',
        'sale_stock',
        'sale_invoices_paid_status',
    ],
    'data': [
        'views/stock_picking_view.xml',
        'views/stock_picking_type.xml',
    ],
    'installable': True,
    'auto_install': False
}
