# -*- coding: utf-8 -*-
{
    'name': "crm_custom",
    'summary': """Customize opportunity forms""",
    'description': """Customize opportunity forms""",
    'author': "jsan-95",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
        'crm',
        'website',
        'website_crm',
    ],
    'data': [
        'data/crm_custom_data.xml',
        'views/crm_lead_views.xml',
        'views/website_crm_templates.xml',
        'views/assets.xml',
    ],
}
