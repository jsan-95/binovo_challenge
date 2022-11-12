# -*- coding: utf-8 -*-
{
    'name': "sales_with_products",
    'summary': """Prevent sales orders with zero product quantity""",
    'description': """""",
    'author': "jsan-95",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'sale',
        'sale_management',
    ],
    'data': [
        'views/sale_views.xml',
    ],
}
